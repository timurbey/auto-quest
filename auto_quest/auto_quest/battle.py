class Battle:
    def __init__(self, characters, affiliation):
        self.characters = characters
        self.affiliation = affiliation

    def run(self):
        battle_log = []
        while not self.done():
            self.characters = self.sort_characters()
            for character in self.characters:
                if character.status():
                    battle_log.append(character.act(self.characters, self.affiliation))
        return battle_log

    # highest value wins sorting; i don't know how to resolve ties
    def sort_characters(self):
        return sorted(self.characters, key = lambda c: c.priority(), reverse = True)

    # true if only one team has living characters; else return false
    def done(self):
        alive = self.affiliation.count() * [False]
        for character in self.characters:
            alive[self.affiliation.of(character.id)] |= character.status()
        return sum(alive) < 2
