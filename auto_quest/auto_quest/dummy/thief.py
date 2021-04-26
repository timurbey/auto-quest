from auto_quest.dummy import Character

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

    def on_no_threat(self, characters, affiliation):
        targets = [
            self.choose(affiliation.enemies(self.id, characters)) for _ in range(2)
        ]

        self.threat += 3
        for target in targets:
            target.health -= 25
        return targets

    def on_threat(self, characters, affiliation):
        self.threat -= 10
        return self
