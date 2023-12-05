"""
vision module
"""


def vision_east(character, current_map, vision_range):
    for vision_range in range(1, 4):
        try:
            map_element = current_map[(
                character["X-coordinate"]+vision_range, character["Y-coordinate"])]
        except KeyError:
            print("There is a wall at your East.")
            break
        else:
            if map_element != "Empty":
                print(
                    f"You can see {map_element} at East {vision_range} step.")


def vision_west(character, current_map, vision_range):
    for vision_range in range(1, 4):
        try:
            map_element = current_map[(
                character["X-coordinate"]-vision_range, character["Y-coordinate"])]
        except KeyError:
            print("There is a wall at your West.")
            break
        else:
            if map_element != "Empty":
                print(
                    f"You can see {map_element} at Wast {vision_range} step.")


def vision_north(character, current_map, vision_range):
    for vision_range in range(1, 4):
        try:
            map_element = current_map[(
                character["X-coordinate"], character["Y-coordinate"]-vision_range)]
        except KeyError:
            print("There is a wall at your North.")
            break
        else:
            if map_element != "Empty":
                print(
                    f"You can see {map_element} at North {vision_range} step.")


def vision_south(character, current_map, vision_range):
    for vision_range in range(1, 4):
        try:
            map_element = current_map[(
                character["X-coordinate"], character["Y-coordinate"]+vision_range)]
        except KeyError:
            print("There is a wall at your South.")
            break
        else:
            if map_element != "Empty":
                print(
                    f"You can see {map_element} at South {vision_range} step.")


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
                'Boss': 'B', 'Oberon': 'B', "Cerberus": "B",
                'Final_boss': 'F',
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
