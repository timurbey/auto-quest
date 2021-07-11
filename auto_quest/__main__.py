from argparse import ArgumentParser
from random import randint

from auto_quest.character import Character, Item
from auto_quest.character.item import ItemType
from auto_quest.util import cli_prompt

def parse_args():
    parser = ArgumentParser()
    return parser.parse_args()

def attack(target):
    target.status['health'] = target.status['health'] - 1

def main():
    args = parse_args()

    id_gen = lambda: randint(1, 1000)

    c = Character(id_gen(), "Dummy", cli_prompt, name = "TOTO")
    c.equip(Item(id_gen(), ItemType.WEAPON, attack))
    c.equip(Item(id_gen(), ItemType.TOOL, None))
    c.equip(Item(id_gen(), ItemType.TRINKET, None))
    c.equip(Item(id_gen(), ItemType.TRINKET, None))

    print(c)
    while c.status['health'] > 0:
        action, target = c.act([c], None)
        action(target)

    print(c)

if __name__ == '__main__':
    main()
