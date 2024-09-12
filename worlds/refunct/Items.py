import typing

from BaseClasses import Item, ItemClassification


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: ItemClassification


class RefunctItem(Item):
    game: str = "Refunct"
    button_nr: int


item_table = {f"Trigger Cluster {i}": ItemData(10 + i, ItemClassification.progression) for i in range(1, 32)}
item_table[":)"] = ItemData(777, ItemClassification.filler)

