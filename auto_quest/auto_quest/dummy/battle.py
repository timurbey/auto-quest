from random import shuffle

# helper class that makes it easy to search for affiliations
class Affiliation:
    def __init__(self, affiliation):
        self.affiliation = affiliation

    def count(self):
        return len(self.affiliation)

    def of(self, id):
        return self.affiliation[id]

    def allies(self, id, characters):
        return [c for c in characters if self.affiliation[id] == self.affiliation[c.id]]

    def enemies(self, id, characters):
        return [c for c in characters if self.affiliation[id] != self.affiliation[c.id]]

# class that manages character turns and checks for a winning team
class Battle:
    def __init__(self, characters, affiliation):
        self.characters = characters
        self.affiliation = affiliation

    def run(self):
        battle_log = []
        turns = 0
        # runs until done or for 10000 turns
        while not self.done() and turns < 10000:
            shuffle(self.characters)
            for character in self.characters:
                if character.status:
                    battle_log.append(character.act(self.characters, self.affiliation))
                    turns += 1
        return battle_log

    # return true if only one team has living members
    def done(self):
        alive = self.affiliation.count() * [False]
        for character in self.characters:
            alive[self.affiliation.of(character.id)] |= character.status
        return sum(alive) < 2
