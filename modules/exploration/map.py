"""
Map module.
"""
import random
import json


def map_list():
    map_1 = {"Description 1": "You enter a grassy meadow.\n"
                              "There is a merchant getting attacked by a group of monsters!\n"
                              "Will you help him?\n",
             "Description 2": "You enter an old dungeon.\n"
                              "You hear skeletons creaking in the distance...surrounding a merchant!\n"
                              "Again? What is this guy doing...\n",
             "Door": [(8, 0), (0, 4), (6, 9)],
             "Chest": [(1, 1), (7, 5)],
             "Enemy": [(6, 1), (2, 3), (3, 4), (1, 5), (2, 5), (4, 5), (6, 5), (3, 6), (4, 6), (7, 6), (2, 7), (2, 9)],
             "Merchant": [(3, 5)]}
    map_2 = {"Description 1": "",
             "Description 2": "",
             "Door": [(5, 0), (4, 9)]}
    map_3 = {"Description 1": "",
             "Description 2": "",
             "Door": [(8, 0), (7, 9)]}
    map_4 = {"Description 1": "",
             "Description 2": "",
             "Door": [(0, 3), (9, 6)]}
    map_5 = {"Description 1": "",
             "Description 2": "",
             "Door": [(3, 0), (9, 7)]}
    map_6 = {"Description 1": "A group of monsters seems to be surrounding something. "
                              "Do you want to go and investigate?\n",
             "Description 2": "A group of monsters fiercely guards treasure chests. "
                              "It's time for a high-risk, high-reward endeavor.\n",
             "Door": [(4, 0), (9, 4), (0, 5), (5, 9)],
             "Chest": [(4, 4), (5, 4), (4, 5), (5, 5)],
             "Enemy": [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1),
                       (1, 2), (2, 2), (3, 2), (4, 2), (5,
                                                        2), (6, 2), (7, 2), (8, 2),
                       (1, 3), (2, 3), (7, 3), (8, 3),
                       (1, 4), (2, 4), (7, 4), (8, 4),
                       (1, 5), (2, 5), (7, 5), (8, 5),
                       (1, 6), (2, 6), (7, 6), (8, 6),
                       (1, 7), (2, 7), (3, 7), (4, 7), (5,
                                                        7), (6, 7), (7, 7), (8, 7),
                       (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8),],
             "Boss": [(5, 3), (4, 6)],
             "Merchant": [(3, 5)],
             "Healing_fountain": [(3, 4), (6, 4), (3, 5), (6, 5)]}
    map_7 = {"Description 1": "You accidentally stumbled into the monsters' lair. But fortunately, "
                              "the number of monsters is not large enough to necessitate a fight for your exit.",
             "Description 2": "The monsters have formed a maze-like formation, but you can "
                              "see a safe path leading to the other side.",
             "Door": [(9, 0), (0, 9)],
             "Chest": [(9, 3), (9, 9)],
             "Enemy": [(3, 0), (3, 1), (7, 1), (7, 2), (8, 2), (9, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3),
                       (5, 4), (7, 4),  (8, 4), (9, 4), (5, 5), (0,
                                                                 6), (1, 6), (3, 6), (6, 6), (3, 7), (7, 7),
                       (3, 8), (6, 8), (3, 9)],
             "Healing_fountain": [(0, 0), (4, 4)]
             }

    map_8 = {"Description 1": "Rumor has it there's a group of monsters known as the 'Newbie Slayers.' "
                              "Never expected to encounter them here.",
             "Description 2": "'Hello, adventurer! Impressive that you've made it this far. Now, let our Four "
                              "Guardians become your opponents!!'",
             "Door": [(0, 0), (0, 9)],
             "Boss": [(0, 4), (0, 5), (0, 6), (0, 7)],
             "Chest": [(0, 2), (0, 3)],
             "Merchant": [(0, 1)]
             }
    map_9 = {"Description 1": "Who has been digging so many holes in the wilderness?",
             "Description 2": "The Chronomancer has altered the structure of this dungeon. "
                              "Conventional knowledge of entrances and exits no longer seems applicable.",
             "Door": [(6, 2), (4, 4), (4, 5), (7, 6), (2, 7)],
             "Chest": [(0, 0), (9, 9)],
             "Enemy": [(3, 0), (6, 0), (9, 0), (0, 2), (3, 3), (9, 4), (0, 5), (5, 6), (0, 9), (0, 3), (0, 7)],
             "Healing_fountain": [(6, 4), (3, 6)]
             }
    map_lucky = {"Description 1": "You discover an abandoned adventurers' guild, and for some reason, the equipment "
                                  "inside has not been taken.\n",
                 "Description 2": "You unexpectedly entered a treasure vault, with a dazzling array of "
                                  "treasures waiting for you.\n",
                 "Door": [(3, 9), (6, 9)],
                 "Chest": [(2, 2), (5, 2), (8, 2), (1, 6), (4, 6), (7, 6)],
                 "Merchant": [(0, 0)],
                 "Healing_fountain": [(4, 4), (6, 4)]
                 }
    map_boss = {"Description": "",
                "Door": [(4, 9), (5, 9)],
                "Final_boss": [(4, 4), (5, 4), (4, 5), (5, 5)],
                "Merchant": [(9, 9)]
                }

    map_list = {1: map_1, 2: map_2, 3: map_3, 4: map_4, 5: map_5,
                6: map_6, 7: map_7, 8: map_8, 9: map_9, 10: map_lucky, 11: map_boss}
    return map_list


def select_map(character_dictionary, map_list):
    if character_dictionary["Character_status"]["Level"] < 3:
        if character_dictionary["Character_status"]["LUK"] > 5:
            map_elements = map_list[random.randint(1, 10)]
        else:
            map_elements = map_list[random.randint(1, 9)]
    else:
        map_elements = map_list[11]
    return map_elements


def describe_current_map(character_dictionary, map_elements):
    if character_dictionary["Character_status"]["Level"] == 1:
        print(map_elements["Description 1"])
    else:
        print(map_elements["Description 2"])


def set_element_on_map(map_elements, element, current_map):
    try:
        map_elements[element]
    except KeyError:
        # print(f"There is no {element} in map_elements.")
        return

    for coordinate in map_elements[element]:
        try:
            current_map[coordinate] = element
        except KeyError:
            print(f"{coordinate} is not in the map.")


def walls(current_map):
    east_wall = 1
    south_wall = 1
    for grid in current_map:
        if grid[0] > east_wall:
            east_wall = grid[0]
        if grid[1] > south_wall:
            south_wall = grid[1]
    return south_wall, east_wall


def create_map(character_dictionary, map_list):
    rows = 10
    columns = 10
    current_map = dict()
    for row in range(rows):
        for column in range(columns):
            coordinate = (column, row)
            current_map[coordinate] = "Empty"
    map_elements = select_map(character_dictionary, map_list)
    describe_current_map(character_dictionary, map_elements)
    element_list = ["Door", "Enemy", "Chest",
                    "Healing_fountain", "Boss", "Final_boss"]
    for element in element_list:
        set_element_on_map(map_elements, element, current_map)
    return current_map    
    