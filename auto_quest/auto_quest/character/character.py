from auto_quest.character.item import ItemType

class Character:
    def __init__(self, id, character_class, logic, name = None):
        # identifiers
        self.id = id
        self.name = name

        # character model
        self.character_class = character_class
        self.equipment = {
            ItemType.WEAPON  : None,
            ItemType.TOOL    : None,
            ItemType.BODY    : None,
            ItemType.HEAD    : None,
            ItemType.FOOT    : None,
            ItemType.TRINKET : [None, None]
        }
        self.logic = logic

        # character status
        self.status = {
            'health'  : 100,
            'effects' : [],
        }

    def __str__(self):
        return str(self.snapshot())

    def snapshot(self):
        return {
            'id'        : self.id,
            'name'      : self.name,
            'class'     : self.character_class,
            'equipment' : self.equipment.copy(),
            'status'    : self.status.copy(),
        }

    def act(self, characters, affiliation):
        return self.logic(self, characters, affiliation)

    # unsure if we need these yet
    @property
    def actions(self):
        return [
            self.equipment[ItemType.WEAPON].effect,
            self.equipment[ItemType.TOOL].effect,
            self.equipment[ItemType.TRINKET][0].effect,
            self.equipment[ItemType.TRINKET][1].effect,
        ]

    def equip(self, item):
        if item.type == ItemType.TRINKET:
            self.equipment[item.type][1] = self.equipment[item.type][0]
            self.equipment[item.type][0] = item
        else:
            self.equipment[item.type] = item
