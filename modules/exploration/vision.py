"""
vision module
"""


def map_element_in_vision(character, current_map, column, row):
    try:
        map_element = current_map[(
            character["X-coordinate"]+column, character["Y-coordinate"]+row)]
    except KeyError:
        map_element = None
    try:
        current_map[(character["X-coordinate"]+column,
                     character["Y-coordinate"])]
    except KeyError:
        map_element = 'EW_wall'
    try:
        current_map[(character["X-coordinate"], character["Y-coordinate"]+row)]
    except KeyError:
        map_element = 'NS_wall'
    return map_element


def print_vision(character, current_map):
    map_icon = {'Empty': ' ', 'Door': 'D', 'Healing_fountain': 'H', 'Enemy': 'E',
                'Boss': 'B', 'Oberon': 'B', "Cerberus": "B", "Dracula": "B",
                'Final Boss': 'F',
                'Chest': 'C', 'Merchant': 'M', 'Character': '#', 'EW_wall': '|', 'NS_wall': '-'}
    for row in range(-character["Character_status"]["VIS"], character["Character_status"]["VIS"]+1):
        print()
        for column in range(-character["Character_status"]["VIS"], character["Character_status"]["VIS"]+1):
            map_element = map_element_in_vision(
                character, current_map, column, row)

            if row == 0 and column == 0:
                map_element = 'Character'

            print(map_icon[map_element], end=' ')
    print()
