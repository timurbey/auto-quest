from auto_quest.dummy import Character
from auto_quest.dummy.actions import medium_attack, weak_attack

# character that hides if it's the threat; has a double medium attack
class Thief(Character):
    counter = 0

    def __init__(self, choice_func = None, eval_func = None):
        super().__init__(
            name = 'thief-' + str(Thief.counter + 1),
            health = 75,
            choice_func = choice_func,
            eval_func = eval_func,
        )
        Thief.counter += 1

    def on_danger(self, characters, affiliation):
        self.threat -= 10
        return self

    def on_threat(self, characters, affiliation):
        target = self.choose(affiliation.enemies(self.id, characters))
        medium_attack(self, target)
        return target

    def on_normal(self, characters, affiliation):
        targets = []
        targets.append(self.choose(affiliation.enemies(self.id, characters)))
        medium_attack(self, targets[-1])
        if len(affiliation.enemies(self.id, characters)) > 0:
            targets.append(self.choose(affiliation.enemies(self.id, characters)))
            weak_attack(self, targets[-1])
        return targets
