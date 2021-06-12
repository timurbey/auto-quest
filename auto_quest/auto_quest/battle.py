class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.characters = []

    def step(self):
        if not self.characters:
            self.characters = sort_characters()
        character = self.characters.pop()
        return character.act(self.player + self.enemy, Affiliation({0: self.player, 1: self.enemy}))

    def run(self):
        battle_log = []
        turns = 0
        while not self.done(): # and turns < 10000:
            self.characters = self.sort_characters()
            for character in self.characters:
                if character.status:
                    battle_log.append(character.act(self.characters, self.affiliation))
                    turns += 1
        return battle_log

    # highest value wins sorting; i don't know how to resolve ties
    def sort_characters(self):
        return sorted(
            self.player + self.enemy,
            key = lambda c: c.priority, reverse = True
        )

    # true if only one team has living characters; else return false
    def done(self):
        alive = self.affiliation.count() * [False]
        for character in self.characters:
            alive[self.affiliation.of(character.id)] |= character.status
        return sum(alive) < 2
