from auto_quest.dummy import Character

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

    def on_no_threat(self, characters, affiliation):
        self.threat += 5
        return self

    def on_threat(self, characters, affiliation):
        target = self.choose(affiliation.enemies(self.id, characters))

        self.threat += 2
        target.health -= 30
        return target
