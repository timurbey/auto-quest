from random import randint

from auto_quest import Character

def action_snapshot(action, user, targets):
    if isinstance(targets, DummyCharacter):
        targets_snapshot = [targets.snapshot()]
    else:
        targets_snapshot = list(map(lambda t: t.snapshot(), targets))
    return [action, user.snapshot(), targets_snapshot]

# randomly chosen based on threat
def choose_character(characters):
    characters.sort(key = lambda c: c.threat)
    target = randint(0, sum(t.threat for t in characters) - 1)
    threat = 0
    for character in characters:
        if target < threat + character.threat:
            return character
        else:
            threat += character.threat

class DummyCharacter(Character):
    counter = 0

    def __init__(self, name, health, speed = 0, choice_func = choose_character):
        self.max_health = health
        self.speed = speed

        self.health = self.max_health
        self.armor = 0
        self.threat = 1

        self.choose = choice_func

        self.name = name
        self.id = DummyCharacter.counter
        DummyCharacter.counter += 1

    # we may not need this anymore now that we moved to snapshots
    def __str__(self):
        return '\n'.join([
            'character: ' + self.name + ' (id=' + str(self.id)  + ')',
            str(self.health) + '/' + str(self.max_health),
            str(self.speed),
            str(self.armor),
        ])

    def id(self):
        return self.id

    def priority(self):
        return self.speed

    def status(self):
        return self.health > 0

    # is this is going to grow forever?
    def snapshot(self):
        return {
            'system': 'dummy',
            'id'    : self.id,
            'name'  : self.name,
            'class' : self.__class__.__name__,
            'health': self.health,
            'armor' : self.armor,
            'threat': self.threat,
        }

    def act(self, characters, affiliation):
        self.begin_turn()

        threat = self.choose(characters)
        if self != threat:
            cmd = self.on_chosen(characters, affiliation)
        else:
            cmd = self.default_action(characters, affiliation)

        self.end_turn()
        return [cmd, [character.snapshot() for character in characters]]

    # turn events
    def begin_turn(self):
        self.threat = max(self.threat // 2, 1)

    def end_turn(self):
        pass

    # mutative actions
    def heal(self, value):
        self.health = min(self.max_health, self.health + value)

    def damage(self, value):
        value = self.armor - value
        self.armor = max(0, value)
        if value < 0:
            self.health = max(0, self.health + value)

    def threaten(self, value):
        self.threat = max(1, self.threat + value)

    def block(self, value):
        self.armor += value
