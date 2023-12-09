"""
vision module
"""


def map_element_in_vision(character: dict, current_map: dict, column: int, row: int) -> str:
    """
    Check whether the element is in character's vision.

    :param character: a dictionary of character attributes
    :param current_map: a dictionary
    :param column: integer
    :param row: integer
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
     items, equipment and debuffs
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: check whether the element is in character's vision
    :return: a string

    >>> character_dictionary_1 = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
    ...                                                 "LUK": 1, "VIS": 3},
    ...                            "Name": "describe", "X-coordinate": 0, "Y-coordinate": 0,
    ...                            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
    ...                            "Equipment": 0, "Debuff": {"Burn": 0}}
    >>> column_1 = 0
    >>> row_1 = -1
    >>> current_map_1 = {(0, 0): "Empty", (1, 0): "Empty", (0, 1): "Empty", (1, 1): "Door"}
    >>> map_element_in_vision(character_dictionary_1, current_map_1, column_1, row_1)
    'NS_wall'

    >>> character_dictionary_1 = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
    ...                                                 "LUK": 1, "VIS": 3},
    ...                            "Name": "describe", "X-coordinate": 0, "Y-coordinate": 0,
    ...                            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
    ...                            "Equipment": 0, "Debuff": {"Burn": 0}}
    >>> column_1 = 1
    >>> row_1 = 1
    >>> current_map_1 = {(0, 0): "Empty", (1, 0): "Empty", (0, 1): "Empty", (1, 1): "Door"}
    >>> map_element_in_vision(character_dictionary_1, current_map_1, column_1, row_1)
    'Door'
    """
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


def print_vision(character: dict, current_map: dict):
    """
    Show Character vision.

    :param character: a dictionary of character attributes
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
     items, equipment and debuffs
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: character vision range is character["Character_status"]["VIS"]
    :postcondition: print every element in character vision range
    """
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
