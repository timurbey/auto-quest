class CharacterStats:
    counter = 0

    def __init__(self, health = 0, speed = 0):
        self.health = health
        self.max_health = health
        self.speed = speed
        self.armor = 0

    def alive(self):
        return self.health > 0

    def heal(self, value):
        self.health = min(self.max_health, self.health + value)

    def damage(self, value):
        value = self.armor - value
        self.armor = max(0, value)
        if value < 0:
            self.health = max(0, self.health + value)

    def block(self, value):
        self.armor += max(value - self.armor, 1)

    def snapshot(self):
        character = CharacterStats(self.max_health, self.speed)
        character.health = self.health
        return character

    def __str__(self):
        return '\n'.join([
            'health:' + str(self.health) + '/' + str(self.max_health),
            'armor:' + str(self.armor),
        ])
