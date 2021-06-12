class Party:
    def __init__(self, characters):
        self.characters = characters

    def __str__(self):
        return ','.join(self.snapshot())

    def snapshot(self):
        return [c.snapshot() for c in self.characters]
