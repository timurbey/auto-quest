from auto_quest import Character

def dummy_policy(user, characters):
    return 0, characters[0]

def attack(user, target):
    target.health = target.health - 1

class DummyCharacter(Character):
    def __init__(self, name, health = 0, actions = None, policy = None):
        super().__init__(name, health, [attack], dummy_policy)
