from auto_quest.dummy import DummyCharacter
from auto_quest.dummy.dummy_character import action_snapshot

class DummyThief(DummyCharacter):
    counter = 0

    def __init__(self):
        super().__init__(
            name = 'thief-' + str(DummyThief.counter + 1),
            health = 75,
            speed = 0
        )
        DummyThief.counter += 1

    def act(self, characters, affiliation):
        self.begin_turn()

        if self == self.choose(characters):
            cmd = [self.vanish()]
        else:
            targets = [self.choose(affiliation.enemies(self.id, characters)) for _ in range(2)]
            cmd = self.attack(targets)

        self.end_turn()
        return [cmd, [character.snapshot() for character in characters]]

    def attack(self, targets):
        self.threaten(3)
        for target in targets:
            target.damage(20)
        return action_snapshot("thief-attack", self, targets)

    def vanish(self):
        self.threaten(-10)
        return action_snapshot("thief-vanish", self, self)
