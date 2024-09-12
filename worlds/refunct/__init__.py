import math
from typing import Dict

from BaseClasses import CollectionState, Entrance, Item, Region, Tutorial

from worlds.AutoWorld import WebWorld, World

from .Items import RefunctItem, item_table
from .Locations import location_table, RefunctLocation
from .Options import RefunctOptions
from .Rules import set_refunct_rules, set_refunct_completion


class RefunctWeb(WebWorld):
    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up Yacht Dice. This guide covers single-player, multiworld, and website.",
            "English",
            "setup_en.md",
            "setup/en",
            ["Spineraks"],
        )
    ]


class RefunctWorld(World):
    """
    Yacht Dice is a straightforward game, custom-made for Archipelago,
    where you cast your dice to chart a course for high scores,
    unlocking valuable treasures along the way.
    Discover more dice, extra rolls, multipliers,
    and unlockable categories to navigate the depths of the game.
    Roll your way to victory by reaching the target score!
    """

    game: str = "Refunct"
    options_dataclass = RefunctOptions

    web = RefunctWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}

    location_name_to_id = {name: data.id for name, data in location_table.items()}

    ap_world_version = "0.0.1"
    
    def generate_early(self) -> None:
        self.itempool = [name for name in item_table]
        self.itempool.remove("Trigger Cluster 1")
        self.multiworld.push_precollected(self.create_item("Trigger Cluster 1"))
            

    def create_items(self):        
        self.multiworld.itempool += [self.create_item(name) for name in self.itempool]

    def create_regions(self):
        # simple menu-board construction
        menu = Region("Menu", self.player, self.multiworld)
        board = Region("Board", self.player, self.multiworld)
        
        board.locations = [
            RefunctLocation(self.player, loc_name, loc_data.id, board, loc_data.button_nr)
            for loc_name, loc_data in location_table.items()
            if loc_data.region == board.name
        ]

        # add the regions
        connection = Entrance(self.player, "New Board", menu)
        menu.exits.append(connection)
        connection.connect(board)
        self.multiworld.regions += [menu, board]
        

    def set_rules(self):
        """
        set rules per location, and add the rule for beating the game
        """
            
        set_refunct_rules(self.multiworld, self.player)
        set_refunct_completion(self.multiworld, self.player)

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = RefunctItem(name, item_data.classification, item_data.code, self.player)
        return item
    