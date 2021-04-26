from auto_quest.dummy import Character

# character that throws a fireball if it's not the threat; has a weak attack
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

    def on_no_threat(self, characters, affiliation):
        targets = affiliation.enemies(self.id, characters)
        self.threat += 5
        for target in targets:
            target.health -= 50
        return targets

    def on_threat(self, characters, affiliation):
        target = self.choose(affiliation.enemies(self.id, characters))

        self.threat += 1
        target.health -= 20
        return target
