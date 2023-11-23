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
                print(f"You can see {map_element} at Wast {vision_range} step.")
                

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
                

def main():
    pass


if __name__ == "__main__":
    main()
