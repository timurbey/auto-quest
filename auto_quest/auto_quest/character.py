class Character:
    def __init__(self, name, health = 0, actions = None, policy = None):
        self.name = name;
        self.max_health = health
        self.health = health
        self.actions = actions
        self.policy = policy

    def act(self, characters):
        if self.actions is None or self.policy is None:
            return False
        idx, target = self.policy(self, characters)
        return self.actions[idx](self, target)
