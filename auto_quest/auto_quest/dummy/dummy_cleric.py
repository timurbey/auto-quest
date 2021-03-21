from auto_quest.dummy import DummyCharacter
from auto_quest.dummy.dummy_character import action_snapshot

class DummyCleric(DummyCharacter):
        counter = 0

        def __init__(self):
            super().__init__(
                name = 'cleric-' + str(DummyCleric.counter + 1),
                health = 75,
                speed = 0
            )
            DummyCleric.counter += 1

        def act(self, characters, affiliation):
            self.begin_turn()

            if self == self.choose(characters):
                cmd = self.shield(affiliation.allies(self.id, characters))
            else:
                target = self.choose(affiliation.enemies(self.id, characters))
                cmd = self.attack(target)

            self.end_turn()
            return [cmd, [character.snapshot() for character in characters]]

        def attack(self, target):
            self.threaten(1)
            target.damage(20)
            return action_snapshot("cleric-attack", self, target)

        def shield(self, targets):
            for target in targets:
                target.block(25)
            return action_snapshot("cleric-shield", self, targets)
