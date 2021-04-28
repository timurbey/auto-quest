from auto_quest.dummy import Character
from auto_quest.dummy.actions import weak_attack

# character that shields its team if it's a threat; has a medium attack
class Cleric(Character):
    counter = 0

    def __init__(self, choice_func = None, eval_func = None):
        super().__init__(
            name = 'cleric-' + str(Cleric.counter + 1),
            health = 75,
            choice_func = choice_func,
            eval_func = eval_func,
        )
        Cleric.counter += 1

    def on_danger(self, characters, affiliation):
        targets = affiliation.allies(self.id, characters)
        for target in targets:
            target.armor += 20
        return targets

    def on_threat(self, characters, affiliation):
        target = self.choose(affiliation.allies(self.id, characters))
        target.armor += 30
        return target

    def on_normal(self, characters, affiliation):
        target = self.choose(affiliation.enemies(self.id, characters))
        weak_attack(self, target)
        return target
