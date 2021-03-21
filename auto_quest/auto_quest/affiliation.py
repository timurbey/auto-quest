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
