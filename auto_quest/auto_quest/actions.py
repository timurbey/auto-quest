def attack(target, value):
    target.status['health'] = target.status['health'] - value

def heal(target, value):
    target.status['health'] = target.status['health'] - value

def defend(target, value):
    target.status['armor'] = target.status['armor'] + value
