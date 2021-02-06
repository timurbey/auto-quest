class Character:
    def __init__(self, id, stats, affiliation):
        self.id = id
        self.stats = stats
        self.affiliation = affiliation

    def act(self, targets):
        raise NotImplementedError()

    def snapshot(self):
        return Character(self.id, self.stats.snapshot(), self.affiliation)

    def __str__(self):
        return '\n'.join([
            'character: ' + self.id['name'] + ' (id=' + str(self.id['id'])  + ')',
            str(self.stats),
            'affiliation:' + str(self.affiliation),
        ])
