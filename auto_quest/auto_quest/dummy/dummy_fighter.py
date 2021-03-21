from auto_quest.dummy import DummyCharacter
from auto_quest.dummy.dummy_character import action_snapshot

class DummyFighter(DummyCharacter):
    counter = 0

    def __init__(self):
        super().__init__(
            name = 'fighter-' + str(DummyFighter.counter + 1),
            health = 100,
            speed = 0
        )
        DummyFighter.counter += 1

    def act(self, characters, affiliation):
        self.begin_turn()

        if self != self.choose(characters):
            cmd = self.taunt()
        else:
            target = self.choose(affiliation.enemies(self.id, characters))
            cmd = self.attack(target)

        self.end_turn()
        return [cmd, [character.snapshot() for character in characters]]

    def attack(self, target):
        self.threaten(2)
        target.damage(25)
        return action_snapshot("fighter-attack", self, target)

    def taunt(self):
        self.threaten(10)
        self.block(10)
        return action_snapshot("fighter-taunt", self, self)
