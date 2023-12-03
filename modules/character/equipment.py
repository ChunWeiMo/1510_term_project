"""
equipment module
"""
import random

character_stats = {"Level": 1, "HP": 100, "STR": 1,
                   "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}


def level1_equipment_list():
    return {1: ["Steel sword", ("STR", 3)],
            2: ["Small round shield", ("DEF", 3)],
            3: ["Cloak", ("SPD", 3)],
            4: ["Cheat coin", ("LUK", 3)],
            5: ["Noble insignia", ("CHR", 3)],
            6: ["The lance of curses", ("STR", 6), ("HP", -30)],
            7: ["Angel's winged garment", ("SPD", 6), ("DEF", -2)],
            8: ["Heavy knight's armor", ("DEF", 6), ("SPD", -2)],
            9: ["Beginner adventurer's guide", ("STR", 1), ("DEF", 1), ("CHR", 1), ("SPD", 1)],
            10: ["Single-barrel telescope", ("VIS", 1)],
            11: ["Giant hammer", ("STR", 5), ("SPD", -1)]
            }


def level2_equipment_list():
    return {1: ["Silver sword", ("STR", 7)],
            2: ["Hero's spear", ("STR", 5), ("SPD", 2)],
            3: ["Hermes shoes", ("SPD", 7)],
            4: ["King's scepter", ("STR", 1), ("CHR", 6)],
            5: ["Kiss of Rose Princess", ("CHR", 7)],
            6: ["Platinum shield", ("DEF", 7)],
            7: ["Oracle crystal ball", ("VIS", 2)],
            8: ["Luxurious carriage", ("SPD", 3), ("CHR", 4)],
            9: ["Spirits guardian", ("DEF", 4), ("SPD", 3)],
            }


def level3_equipment_list():
    return {1: ["Ragnarök", ("STR", 15)],
            2: ["The Goddess's blessing", ("DEF", 15)],
            3: ["Garuda's wing", ("SPD", 15)],
            4: ["Dragon slayer", ("STR", 10),("STR", 5)]
            }


def get_equipment(character_dictionary):
    if character_dictionary['Character_status']['Level'] == 1:
        equipments = level1_equipment_list()
    elif character_dictionary['Character_status']['Level'] == 2:
        equipments = level2_equipment_list()
    else:
        equipments = level3_equipment_list()

    while True:
        equipment_number = random.randint(1, 99)
        if equipment_number in equipments:
            equipment = equipments[equipment_number]
            break
    print(f"You find {equipment[0]}!")
    print(f"Ability of {equipment[0]}:")
    for ability in equipment[1:]:
        print(f"{ability[0]} {ability[1]}")
    print()
    return equipment, equipment_number


def use_equipment(character_dictionary, equipment, equipment_number):
    character_dictionary["Equipment"] = equipment_number
    for ability in equipment[1:]:
        if ability[0] in character_dictionary['Character_status']:
            character_dictionary['Character_status'][ability[0]] += ability[1]
