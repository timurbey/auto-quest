from auto_quest.dummy import Character
from auto_quest.dummy.actions import weak_attack

class Mage(Character):
    counter = 0

    def __init__(self, choice_func = None, eval_func = None):
        super().__init__(
            name = 'mage-' + str(Mage.counter + 1),
            health = 50,
            choice_func = choice_func,
            eval_func = eval_func,
        )
        Mage.counter += 1

    def on_danger(self, characters, affiliation):
        self.armor += 40
        return self

    def on_threat(self, characters, affiliation):
        target = self.choose(affiliation.enemies(self.id, characters))
        weak_attack(self, target)
        return target

    def on_normal(self, characters, affiliation):
        targets = affiliation.enemies(self.id, characters)[:5]
        for target in targets:
            weak_attack(self, target)
        return targets
