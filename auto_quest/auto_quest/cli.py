from pprint import pprint

def cli_prompt(self, characters, affiliation):
    pprint(dict(enumerate(map(lambda c: c.snapshot(), characters))))
    pprint(self.actions)
    action_idx = int(input("Choose an action (1 - 4): "))
    action = self.actions[action_idx - 1]
    target = characters[int(input(f"Choose a target (1 - {len(characters)}): ")) - 1]
    return action, target
