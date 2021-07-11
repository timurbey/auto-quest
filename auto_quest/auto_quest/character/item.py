from enum import auto, Enum

class Item:
    def __init__(self, id, type, effect, name = None):
        # identifiers
        self.id = id
        self.name = name

        # item model
        self.type = type
        self.effect = effect

    def __str__(self):
        return str(self.snapshot())

    def snapshot(self):
        return {
            'id'      : self.id,
            'name'    : self.name,
            'type'    : self.type,
            'effect' : self.effect,
        }

class ItemType(Enum):
    WEAPON  = auto()
    TOOL    = auto()
    BODY    = auto()
    HEAD    = auto()
    FOOT    = auto()
    TRINKET = auto()
