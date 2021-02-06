class AutoBattle:
    def __init__(self, characters):
        self.characters = characters

    def run(self):
        log = []
        queued = self.characters.copy()
        queued.sort(key = lambda c: c.stats.speed)
        done = []
        while not self.done():
            if not queued:
                queued = done
                queued.sort(key = lambda c: c.stats.speed)
                done = []
            character = queued.pop()
            log.append(character.act(self.characters))
            done.append(character)
        return log

    def done(self):
        affiliations = len({c.affiliation for c in self.characters})
        alive = affiliations * [False]
        for character in self.characters:
            if character.stats.alive():
                alive[character.affiliation] = True

        return sum(alive) < 2
