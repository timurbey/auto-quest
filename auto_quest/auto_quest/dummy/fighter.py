from auto_quest.dummy import Character
from auto_quest.dummy.actions import medium_attack, strong_attack

# character that taunts if they aren't the threat; has a strong attack
class Fighter(Character):
    counter = 0

    def __init__(self, choice_func = None, eval_func = None):
        super().__init__(
            name = 'fighter-' + str(Fighter.counter + 1),
            health = 100,
            choice_func = choice_func,
            eval_func = eval_func,
        )
        Fighter.counter += 1

    def on_danger(self, characters, affiliation):
        target = self.choose(affiliation.enemies(self.id, characters))
        strong_attack(self, target)
        return target

    def on_threat(self, characters, affiliation):
        target = self.choose(affiliation.enemies(self.id, characters))
        medium_attack(self, target)
        return target

    def on_normal(self, characters, affiliation):
        self.threat += 5
        self.armor += 30
        return self
