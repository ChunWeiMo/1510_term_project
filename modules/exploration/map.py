"""
Map module.
"""
import random


def maps() -> dict:
    """
    Create a dictionary of 10 maps with description and map elements.

    :postcondition: create a dictionary of 10 maps with description and map elements
    :return: a dictionary
    """
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
    map_2 = {"Description 1": "There is a big hill and a tall tree in the distance.\n"
                              "Perhaps there is some treasure under it's roots?",
             "Description 2": "The room you enter smells damp and moldy.\n"
                              "It's dark and hard to see where you are going.",
             "Door": [(5, 0), (4, 9)],
             "Chest": [(0, 0), (0, 3), (8, 5)],
             "Enemy": [(2, 2), (0, 8), (2, 6), (5, 7), (7, 2), (8, 6), (9, 9)],
             "Merchant": [(4, 4)]}
    map_3 = {"Description 1": "You wander into a dark forest.\n"
                              "What is wrong with this place! It's swarming with enemies!",
             "Description 2": "You enter the room and immediately feel the heat increase.\n"
                              "What's going on in here? The walls are crusted in what looks like cooled lava...",
             "Door": [(8, 0), (7, 9)],
             "Chest": [(5, 2), (2, 7)],
             "Healing_fountain": [(8, 5)],
             "Cerberus": [(5, 6)],
             "Enemy": [(0, 1), (2, 1), (3, 4), (1, 9), (3, 9), (6, 3), (9, 3), (9, 5)]}
    map_4 = {"Description 1": "You find a clearing surrounded by shining lights.\n"
                              "It looks like some monsters are having a party here.",
             "Description 2": "You shudder at what you see when you walk through the door.\n"
                              "There is a dark ritual going on this this room, "
                              "the monsters keep circling and dancing around some treasure.",
             "Door": [(0, 3), (9, 6)],
             "Chest": [(4, 4), (4, 5), (5, 4), (5, 5)],
             "Enemy": [(1, 0), (2, 0), (3, 1), (4, 1), (9, 1), (5, 2), (9, 2), (4, 3),
                       (5, 3), (2, 4), (3, 4), (6, 4), (8, 4), (1, 5), (3, 5), (6, 5),
                       (7, 5), (1, 6), (4, 6), (5, 6), (0, 7), (4, 7), (0, 8), (5, 8), (6, 8), (7, 9), (8, 9)]}
    map_5 = {"Description 1": "The grassland ends abruptly and an old battlefield lies in front of you.\n"
                              "There's some treasure to be found here...",
             "Description 2": "You were just in a dark hallway but suddenly this room becomes light and airy "
                              "as if you just walked into a field of flowers.\nWhat kind of illusion is this??!",
             "Door": [(3, 0), (9, 7)],
             "Chest": [(6, 2), (1, 4), (4, 7)],
             "Healing_fountain": [(7, 9)],
             "Oberon": [(5, 4)],
             "Enemy": [(1, 2), (0, 7), (2, 7), (4, 4), (4, 9), (8, 1), (7, 7)]}
    map_6 = {"Description 1": "A group of monsters seems to be surrounding something. "
                              "Do you want to go and investigate?\n",
             "Description 2": "A group of monsters fiercely guards treasure chests. "
                              "It's time for a high-risk, high-reward endeavor.\n",
             "Door": [(4, 0), (9, 4), (0, 5), (5, 9)],
             "Chest": [(4, 4), (5, 4), (4, 5), (5, 5)],
             "Enemy": [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1),
                       (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2),
                       (1, 3), (2, 3), (7, 3), (8, 3), (1, 4), (2, 4), (7, 4), (8, 4),
                       (1, 5), (2, 5), (7, 5), (8, 5), (1, 6), (2, 6), (7, 6), (8, 6),
                       (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7),
                       (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)],
             "Dracula": [(5, 3), (4, 6)],
             "Merchant": [(3, 5)],
             "Healing_fountain": [(3, 4), (6, 4), (3, 5), (6, 5)]}
    map_7 = {"Description 1": "You accidentally stumbled into the monsters' lair. But fortunately, "
                              "the number of monsters is not large enough to necessitate a fight for your exit.",
             "Description 2": "The monsters have formed a maze-like formation, but you can "
                              "see a safe path leading to the other side.",
             "Door": [(9, 0), (0, 9)],
             "Chest": [(9, 3), (9, 9)],
             "Enemy": [(3, 0), (3, 1), (7, 1), (7, 2), (8, 2), (9, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3),
                       (5, 4), (7, 4), (8, 4), (9, 4), (5, 5), (0,
                                                                6), (1, 6), (3, 6), (6, 6), (3, 7), (7, 7),
                       (3, 8), (6, 8), (3, 9)],
             "Healing_fountain": [(0, 0), (4, 4)]
             }

    map_8 = {"Description 1": "Rumor has it there's a group of monsters known as the 'Newbie Slayers.' "
                              "Never expected to encounter them here.",
             "Description 2": "'Hello, adventurer! Impressive that you've made it this far. Now, let our Four "
                              "Guardians become your opponents!!'",
             "Door": [(5, 0), (5, 9)],
             "Enemy": [(4, 4), (5, 5), (4, 6), (5, 7)],
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
                "Final Boss": [(4, 4), (5, 4), (4, 5), (5, 5)],
                "Merchant": [(9, 9)]
                }

    map_list = {1: map_1, 2: map_2, 3: map_3, 4: map_4, 5: map_5,
                6: map_6, 7: map_7, 8: map_8, 9: map_9, 10: map_lucky, 11: map_boss}
    return map_list


def select_map(character_dictionary: dict, map_list: dict) -> dict:
    """
    Return a random map elements according to character level and lucky.

    :param character_dictionary: a dictionary of character attributes
    :param map_list: a dictionary of 10 map
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
     items, equipment and debuffs
    :precondition: the key of map_list is description or map elements
    :precondition: the value of map_list is the content description or coordinate
    :return: a dictionary
    """
    if character_dictionary["Character_status"]["Level"] < 3:
        if character_dictionary["Character_status"]["LUK"] > 5:
            map_elements = map_list[random.randint(1, 10)]
        else:
            map_elements = map_list[random.randint(1, 9)]
    else:
        map_elements = map_list[11]
    return map_elements


def describe_current_map(character_dictionary: dict, map_elements: dict):
    """
    Print the description of the map.

    :param character_dictionary: a dictionary of character attributes
    :param map_elements: a dictionary of map elements
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
     items, equipment and debuffs
    :precondition: map_element must have key Description 1 and Description 2
    :procondition: print the description of the map
    """
    if character_dictionary["Character_status"]["Level"] == 1:
        print(map_elements["Description 1"])
    elif character_dictionary["Character_status"]["Level"] == 2:
        print(map_elements["Description 2"])
    else:
        print("You finally enter the boss' chambers.\nIn the middle you see a huge dragon, yawning and blinking"
              " as if it just woke up.\nThe doors shut behind you with a loud bang, notifying the creature of "
              "your arrival.")


def set_element_on_map(map_elements: dict, element: str, current_map: dict):
    """
    Set elements on current map.

    :param map_elements: a dictionary of map elements
    :param element: a string
    :param current_map: a dictionary
    :precondition: map_element must have element and a list of coordinate as key-value pairs
    :precondition: element must be a string
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: change Empty to element if there is an element at the coordinate

    >>> element_1 = "Door"
    >>> current_map_1 = {(0, 0): 'Empty', (1, 0): 'Empty', (0, 1): 'Empty', (1, 1): 'Empty'}
    >>> map_elements_1 = {'Door': [(0, 0)]}
    >>> set_element_on_map(map_elements_1, element_1, current_map_1)
    >>> current_map_1
    {(0, 0): 'Door', (1, 0): 'Empty', (0, 1): 'Empty', (1, 1): 'Empty'}

    >>> element_1 = "Enemy"
    >>> current_map_1 = {(0, 0): 'Empty', (1, 0): 'Empty', (2, 0): 'Empty', (0, 1): 'Empty', (1, 1): 'Empty',
    ...                  (2, 1): 'Empty'}
    >>> map_elements_1 = {'Enemy': [(1, 1), (0, 1)]}
    >>> set_element_on_map(map_elements_1, element_1, current_map_1)
    >>> current_map_1
    {(0, 0): 'Empty', (1, 0): 'Empty', (2, 0): 'Empty', (0, 1): 'Enemy', (1, 1): 'Enemy', (2, 1): 'Empty'}
    """
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


def walls(current_map: dict) -> tuple:
    """
    Return the boundaries of the current map.

    :param current_map: a dictionary
    :precondition: key is a tuple that contains a set of coordinates
    :postcondition: get the boundary of the current map
    :return: a tuple
    >>> current_map_1 = {(0, 0): 'Empty', (0, 1): 'Empty', (1, 0): 'Empty', (1, 1): 'Empty'}
    >>> walls(current_map_1)
    (1, 1)

    >>> current_map_1 = {(0, 0): 'Empty', (0, 1): 'Empty', (1, 0): 'Empty', (1, 1): 'Empty',(2, 0): 'Empty',
    ... (2, 1): 'Empty'}
    >>> walls(current_map_1)
    (1, 2)
    """
    east_wall = 1
    south_wall = 1
    for grid in current_map:
        if grid[0] > east_wall:
            east_wall = grid[0]
        if grid[1] > south_wall:
            south_wall = grid[1]
    return south_wall, east_wall


def create_map(character_dictionary: dict, map_list: dict) -> dict:
    """
    Create a map with map elements.

    :param character_dictionary: a dictionary of character attributes
    :param map_list: a dictionary of 10 map
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
     items, equipment and debuffs
    :precondition: the key of map_list is description or map elements
    :precondition: the value of map_list is the content description or coordinate
    :postcondition: create a map with map elements
    :return: a dictionary
    """
    rows = 10
    columns = 10
    current_map = {(column, row): "Empty" for row in range(rows) for column in range(columns)}
    map_elements = select_map(character_dictionary, map_list)
    describe_current_map(character_dictionary, map_elements)
    element_list = ["Door", "Enemy", "Chest", "Merchant",
                    "Healing_fountain", "Boss", "Final Boss", "Oberon", "Cerberus", "Dracula"]
    for element in element_list:
        set_element_on_map(map_elements, element, current_map)
    return current_map
