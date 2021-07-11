from pprint import pprint

def cli_prompt(character, characters, affiliation):
    pprint(dict(enumerate(map(lambda c: c.snapshot(), characters))))
    pprint(character.actions)
    action_idx = int(input("Choose an action (1 - 4): "))
    action = character.actions[action_idx - 1]
    target = characters[int(input(f"Choose a target (1 - {len(characters)}): ")) - 1]
    return action, target
