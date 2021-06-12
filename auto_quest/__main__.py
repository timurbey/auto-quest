from argparse import ArgumentParser
from random import randint

from auto_quest import Character, Item
from auto_quest.cli import cli_prompt
from auto_quest.item import ItemType

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--dummy', action='store_true')
    return parser.parse_args()

def damage(c, value):
    c.status['health'] = c.status['health'] - value

def main():
    # args = parse_args()

    # TODO(timur): add hooks for custom logic
    # if args.dummy:
    #     run_dummy_tournament()

    id = lambda: randint(1, 1000)

    c = Character(id(), "Dummy", cli_prompt, name = "Timur")
    c.equip(Item(id(), ItemType.WEAPON, [lambda c: damage(c, 1)]))
    c.equip(Item(id(), ItemType.TOOL, [lambda: 1]))
    c.equip(Item(id(), ItemType.TRINKET, [lambda: 1]))
    c.equip(Item(id(), ItemType.TRINKET, [lambda: 1]))

    while c.status['health'] > 0:
        action, target = c.act([c], None)
        [a(target) for a in action]

if __name__ == '__main__':
    main()
