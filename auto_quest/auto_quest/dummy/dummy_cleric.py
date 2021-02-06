from random import choice

from auto_quest import Character
from auto_quest import CharacterStats
from auto_quest.dummy import DummyCharacter

class DummyCleric(DummyCharacter):
    def __init__(self, affiliation):
        super().__init__(
            health = 75,
            speed = 0,
            affiliation = affiliation)
        self.id['name'] = '-'.join(['cleric', str(self.id['id'])])

    def act(self, characters):
        targets = [c for c in characters if c.affiliation == self.affiliation and c.stats.health < 25]
        if targets:
            cmd = self.heal(min(targets, key = lambda c: c.stats.health))
        else:
            cmd = self.attack(choice([c for c in characters if c.affiliation != self.affiliation]))
        return [cmd, [character.snapshot() for character in characters]]

    def attack(self, target):
        target.stats.damage(20)
        return [self.attack, self, target]

    def heal(self, target):
        target.stats.heal(25)
        return [self.heal, self, target]
