from random import choice

from auto_quest import Character
from auto_quest import CharacterStats
from auto_quest.dummy import DummyCharacter

class DummyThief(DummyCharacter):
    def __init__(self, affiliation):
        super().__init__(
            health = 75,
            speed = 1,
            affiliation = affiliation)
        self.id['name'] = '-'.join(['thief', str(self.id['id'])])

    def act(self, characters):
        cmd = self.attack([
            choice([c for c in characters if c.affiliation != self.affiliation]),
            choice([c for c in characters if c.affiliation != self.affiliation])
        ])
        return [cmd, [character.snapshot() for character in characters]]

    def attack(self, targets):
        for target in targets:
            target.stats.damage(35)
        return [self.attack, self, targets]
