from random import choice

from auto_quest import Character
from auto_quest import CharacterStats

class DummyCharacter(Character):
    counter = 0

    def __init__(self, health, speed, affiliation):
        super().__init__(
            id = {
                  'id': DummyCharacter.counter,
                  'name': 'dummy-' + str(DummyCharacter.counter)
            },
            stats = CharacterStats(health = health, speed = speed),
            affiliation = affiliation
        )
        DummyCharacter.counter += 1
