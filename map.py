import random


def make_maps():
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
             "Description 2": ""}
    map_3 = {"Description 1": "",
             "Description 2": ""}
    map_4 = {"Description 1": "",
             "Description 2": ""}
    map_5 = {"Description 1": "",
             "Description 2": ""}
    map_6 = {"Description 1": "",
             "Description 2": ""}
    map_7 = {"Description 1": "",
             "Description 2": ""}
    map_8 = {"Description 1": "",
             "Description 2": ""}
    map_9 = {"Description 1": "",
             "Description 2": ""}
    map_lucky = {"Description 1": "",
                 "Description 2": ""}
    map_boss = {"Description": ""}

    map_list = {1: map_1, 2: map_2, 3: map_3, 4: map_4, 5: map_5,
                6: map_6, 7: map_7, 8: map_8, 9: map_9, 10: map_lucky, 11: map_boss}
    return map_list


def select_map(character, map_list):
    if character["LUK"] > 5:
        current_map = map_list[random.randint(1, 10)]
    else:
        current_map = map_list[random.randint(1, 9)]
    return current_map


def describe_current_map(character, current_map):
    if character["Level"] == 1:
        print(current_map["Description 1"])
    else:
        print(current_map["Description 2"])
