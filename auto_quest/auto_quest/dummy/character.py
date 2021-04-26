from enum import Enum
from random import randint

# creates a snapshot that contains an action name, user, and target(s).
def action_snapshot(action, user, targets):
    if isinstance(targets, Character):
        targets_snapshot = [targets.snapshot()]
    else:
        targets_snapshot = list(map(lambda t: t.snapshot(), targets))
    return [action, user.snapshot(), targets_snapshot]

# chooses a character based on cumulative threat
def choose_character(characters):
    characters.sort(key = lambda c: c.threat)
    target = randint(0, sum(t.threat for t in characters) - 1)
    threat = 0
    for character in characters:
        if target < threat + character.threat:
            return character
        else:
            threat += character.threat

def evaluate_character(is_self):
    if is_self:
        return State.THREAT
    else:
        return State.NORMAL

class State(Enum):
    DEAD = 0
    NORMAL = 1
    THREAT = 2
    DANGER = 3

# prototype class for characters with hooks for the logic and actions
class Character:
    counter = 0

    def __init__(self, name = None, health = 1, choice_func = None, eval_func = None):
        # set up character
        self._health = health
        self._armor = 0
        self._threat = 1

        # set up logic
        if choice_func is None:
            self.choose = choose_character
        else:
            self.choose = choice_func

        if eval_func is None:
            self.evaluate = lambda c: evaluate_character(self == self.choose(c))
        else:
            self.evaluate = eval_func

        self.id = Character.counter
        if name is None:
            name = str(self.id)
        else:
            self.name = name
        Character.counter += 1

    def __str__(self):
        return str(self.snapshot())

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

    @property
    def health(self):
        return self._health

    def damage(self, value):
        excess = value - self._armor
        if excess > 0:
            self._armor = 0
            self._health = max(0, self._health - excess)
        else:
            self._armor = self._armor - value

    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, value):
        self._armor = max(0, value)

    @property
    def threat(self):
        return self._threat

    @threat.setter
    def threat(self, value):
        self._threat = max(1, value)

    def act(self, characters, affiliation):
        self.threat = self.threat // 2
        self.armor = 0

        # TODO(timur): add more states
        state = self.evaluate(characters)
        if state is State.THREAT:
            action = self.on_threat(characters, affiliation)
        elif state is State.NORMAL:
            action = self.on_no_threat(characters, affiliation)
        cmd = action_snapshot(
            self.__class__.__name__ + "@" + str(state),
            self,
            action
        )

        return [cmd, [character.snapshot() for character in characters]]
