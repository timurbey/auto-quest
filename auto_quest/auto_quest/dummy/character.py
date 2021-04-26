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

# prototype class for characters with hooks for the logic and actions
class Character:
    counter = 0

    def __init__(self, name = None, health = 1, choice_func = None, eval_func = None):
        # set up character
        self._health = health
        self._threat = 1

        # set up logic
        if choice_func is None:
            self.choose = choose_character
        else:
            self.choose = choice_func

        if eval_func is None:
            self.evaluate = lambda c: self == self.choose(c)
        else:
            self.evaluate = eval_func

        self._id = Character.counter
        if name is None:
            name = str(self._id)
        else:
            self.name = name
        Character.counter += 1

    def __str__(self):
        return str(self.snapshot())

    @property
    def id(self):
        return self._id

    @property
    def status(self):
        return self._health > 0

    def snapshot(self):
        return {
            'system': 'dummy',
            'id'    : self._id,
            'name'  : self.name,
            'class' : self.__class__.__name__,
            'health': self.health,
            'threat': self.threat,
        }

    # accessors for health and threat
    @property
    def health(self):
        return self._health

    @property
    def threat(self):
        return self._threat

    @health.setter
    def health(self, value):
        self._health = max(0, value)

    @threat.setter
    def threat(self, value):
        self._threat = max(1, value)

    def act(self, characters, affiliation):
        self.threat = max(self.threat // 2, 1)

        if self.evaluate(characters):
            cmd = action_snapshot(
                self.__class__.__name__ + "-on_threat",
                self,
                self.on_threat(characters, affiliation)
            )
        else:
            cmd = action_snapshot(
                self.__class__.__name__ + "-on_no_threat",
                self,
                self.on_no_threat(characters, affiliation)
            )

        return [cmd, [character.snapshot() for character in characters]]
