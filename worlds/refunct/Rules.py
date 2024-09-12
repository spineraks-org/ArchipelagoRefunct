from BaseClasses import MultiWorld

required_buttons = {
    13: [3, 11, 14, 15, 23, 24, 27],
    16: [2, 17, 28],
    18: [8],
    22: [3, 11, 12, 20, 30],
}

def set_refunct_rules(world: MultiWorld, player: int):
    for location in world.get_locations(player):  
        if location.name.startswith("Button"):
            button_nr = location.name.split("Button ")[1]
            buttons = []
            if button_nr in required_buttons:
                buttons = required_buttons[button_nr]
            location.access_rule = lambda state, player=player, button_nr=button_nr, buttons=buttons: all([
                state.has(f"Trigger Cluster {button_nr}", player, 1),
                any(state.has(f"Trigger Cluster {i}", player, 1) for i in buttons) or not buttons
            ])
            

def set_refunct_completion(world: MultiWorld, player: int):
    world.completion_condition[player] = lambda state: state.has("Trigger Cluster 31", player)