from auto_quest.dummy import DummyCharacter
from auto_quest.dummy.dummy_character import action_snapshot

class DummyMage(DummyCharacter):
    counter = 0

    def __init__(self):
        super().__init__(
            name = 'mage-' + str(DummyMage.counter + 1),
            health = 50,
            speed = 0
        )
        DummyMage.counter += 1

    def act(self, characters, affiliation):
        self.begin_turn()

        if self != self.choose(characters):
            cmd = self.fireball(characters)
        else:
            target = self.choose(affiliation.enemies(self.id, characters))
            cmd = self.attack(target)

        self.end_turn()
        return [cmd, [character.snapshot() for character in characters]]

    def attack(self, target):
        self.threaten(1)
        target.damage(20)
        return action_snapshot("mage-attack", self, target)

    def fireball(self, targets):
        self.threaten(5)
        for target in targets:
            target.damage(50)
        return action_snapshot("mage-fireball", self, targets)
