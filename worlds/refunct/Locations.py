import typing

from BaseClasses import Location
    
class LocData(typing.NamedTuple):
    id: int
    button_nr: int
    region: str
    
class RefunctLocation(Location):
    game: str = "Refunct"
    button_nr: int

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent, button_nr):
        super().__init__(player, name, address, parent)

location_table = {f"Button {i}": LocData(10 + i, i, "Board") for i in range(1, 32)}