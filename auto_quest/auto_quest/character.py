class Character:
    def id(self):
        raise NotImplementedError()

    def priority(self):
        raise NotImplementedError()

    def status(self):
        raise NotImplementedError()

    def snapshot(self):
        raise NotImplementedError()

    def act(self, characters, affiliation):
        raise NotImplementedError()
