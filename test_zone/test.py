import character
import map
import random
import vision


def main():
    map_list = map.make_maps()
    # map_element = map.select_map(character, map_list)

    # map.describe_current_map(character, map_element)

    rows = 10
    columns = 10
    current_map = dict()
    for row in range(rows):
        for column in range(columns):
            coordinate = (column, row)
            current_map[coordinate] = "Empty"

    map_elements = map_list[9]
    map.set_element_on_map(map_elements, "Door", current_map)
    map.set_element_on_map(map_elements, "Enemy", current_map)
    map.set_element_on_map(map_elements, "Chest", current_map)
    map.set_element_on_map(map_elements, "Healing_fountain", current_map)
    map.set_element_on_map(map_elements, "Boss", current_map)
    map.set_element_on_map(map_elements, "Final_boss", current_map)
    # print(current_map)
    # for coordinate in current_map:
    #     print(coordinate)
    # south_wall, east_wall = map.walls(current_map)

    character_status = {'Level': 1, 'HP': 100, 'STR': 10,
                        'DEF': 1, 'CHR': 1, 'SPD': 1, 'LUK': 2}
    character_1 = {"character_status": character_status,
                   "X-coordinate": 1, "Y-coordinate":5}

    # character.start_from_door(map_elements, character_1)
    # print(character_1)
    
    # ==================
    # test standing
    # ==================
    # if current_map[(character_1["X-coordinate"], character_1["Y-coordinate"])] != "Empty":
    #     print(
    #         f'You meet {current_map[(character_1["X-coordinate"], character_1["Y-coordinate"])]}')

    # character.describe_current_location(current_map, character_1)
    # vision_range = 3
    # vision.print_vision(character_1, current_map, vision_range)
    # print()
    
    # ==================
    # test text vision
    # ==================
    # vision.vision_north(character_1, current_map, vision_range)
    # vision.vision_east(character_1, current_map, vision_range)
    # vision.vision_south(character_1, current_map, vision_range)
    # vision.vision_west(character_1, current_map, vision_range)

    # ==================
    # test moving
    # ==================
    direction = 0
    vision_range = 3
    while direction!= 5:
        character.describe_current_location(current_map, character_1)
        vision.print_vision(character_1, current_map, vision_range)
        print()
        direction = int(input("Enter a direction: "))
        can_move = character.validate_move(current_map, character_1, direction)
        if can_move:
            character.move_character(character_1, direction)
            # print(character_1)
        if current_map[(character_1["X-coordinate"], character_1["Y-coordinate"])] != "Empty":
            print(
                f'You meet {current_map[(character_1["X-coordinate"], character_1["Y-coordinate"])]}')

        

if __name__ == "__main__":
    main()
