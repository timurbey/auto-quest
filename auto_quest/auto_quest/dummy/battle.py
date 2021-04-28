from random import shuffle

# class that makes it easy to search for affiliations
class Affiliation:
    def __init__(self, affiliation):
        self.affiliation = affiliation

    def count(self):
        return len(self.affiliation)

    def of(self, id):
        return self.affiliation[id]

    def allies(self, id, characters):
        return [c for c in characters if self.affiliation[id] == self.affiliation[c.id] and c.health > 0]

    def enemies(self, id, characters):
        return [c for c in characters if self.affiliation[id] != self.affiliation[c.id] and c.health > 0]

# class that manages character turns and checks for a winning team
class Battle:
    def __init__(self, characters, affiliation):
        self.characters = characters
        self.affiliation = affiliation

    def run(self):
        turns = []
        while not self.done():
            shuffle(self.characters)
            for c in self.characters:
                if self.done():
                    break
                if c.health > 0:
                    turns.append(c.act(self.characters, self.affiliation))
        return turns

    # return true if only one team has living members
    def done(self):
        alive = self.affiliation.count() * [False]
        for c in self.characters:
            alive[self.affiliation.of(c.id)] |= c.health > 0
        return sum(alive) < 2
