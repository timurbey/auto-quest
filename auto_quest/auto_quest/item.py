from enum import auto, Enum
from random import randint

class Item:
    def __init__(self, id, type, effects, name = None):
        # identifiers
        self.id = id
        self.name = name

        # item model
        self.type = type
        self.effects = effects

    def __str__(self):
        return str(self.snapshot())

    def snapshot(self):
        return {
            'id'      : self.id,
            'name'    : self.name,
            'type'    : self.type,
            'effects' : self.effects,
        }

class ItemType(Enum):
    WEAPON  = auto()
    TOOL    = auto()
    BODY    = auto()
    HEAD    = auto()
    FOOT    = auto()
    TRINKET = auto()
