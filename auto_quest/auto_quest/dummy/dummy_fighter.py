from random import choice

from auto_quest import Character
from auto_quest import CharacterStats
from auto_quest.dummy import DummyCharacter

class DummyFighter(DummyCharacter):
    def __init__(self, affiliation):
        super().__init__(
            health = 100,
            speed = 0,
            affiliation = affiliation)
        self.id['name'] = '-'.join(['fighter', str(self.id['id'])])

    def act(self, characters):
        if self.stats.armor == 0:
            cmd = self.block()
        else:
            cmd = self.attack(choice([c for c in characters if c.affiliation != self.affiliation]))
        return [cmd, [character.snapshot() for character in characters]]

    def attack(self, target):
        target.stats.damage(25)
        return [self.attack, self, target]

    def block(self):
        self.stats.block(3)
        return [self.block, self, self]
