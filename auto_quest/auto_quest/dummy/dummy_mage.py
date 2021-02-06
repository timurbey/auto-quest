from random import random, choice

from auto_quest import Character
from auto_quest import CharacterStats
from auto_quest.dummy import DummyCharacter

class DummyMage(DummyCharacter):
    def __init__(self, affiliation):
        super().__init__(
            health = 50,
            speed = 0,
            affiliation = affiliation)
        self.id['name'] = '-'.join(['mage', str(self.id['id'])])

    def act(self, characters):
        if random() > 0.25:
            cmd = self.attack(choice([c for c in characters if c.affiliation != self.affiliation]))
        else:
            cmd = self.fireball([c for c in characters if c.affiliation != self.affiliation])
        return [cmd, [character.snapshot() for character in characters]]

    def attack(self, target):
        target.stats.damage(50)
        return [self.attack, self, target]

    def fireball(self, targets):
        for target in targets:
            target.stats.damage(25)
        return [self.fireball, self, targets]
