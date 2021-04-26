from auto_quest.dummy import Character

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

    def on_no_threat(self, characters, affiliation):
        target = self.choose(affiliation.enemies(self.id, characters))

        self.threat += 1
        target.damage(25)
        return target

    def on_threat(self, characters, affiliation):
        targets = affiliation.allies(self.id, characters)
        for target in targets:
            target.armor += 20
        return targets
