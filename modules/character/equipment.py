"""
equipment module
"""
import random


def level1_equipment_list():
    """
    Return level 1 equipments list.

    :postcondition: generate a dictionary of level 1 equipment with name and buff/debuff
    :return: a dictionary
    """
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
    """
    Return level 2 equipments list.

    :postcondition: generate a dictionary of level 2 equipment with name and buff/debuff
    :return: a dictionary
    """
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
    """
    Return level 3 equipments list.

    :postcondition: generate a dictionary of level 2 equipment with name and buff/debuff
    :return: a dictionary
    """
    return {1: ["Ragnarök", ("STR", 15)],
            2: ["The Goddess's blessing", ("DEF", 15)],
            3: ["Garuda's wing", ("SPD", 15)],
            4: ["Dragon slayer", ("STR", 10), ("STR", 5)]
            }


def get_equipment(character_dictionary: dict) -> list:
    """
    Return equipment according to character's level.

    :param character_dictionary: a dictionary of character attributes
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
     items, equipment and debuffs
    :postcondition: randomly get equipment according to character's level
    :return: a dictionary
    """
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
    print(f"Sweet...You find {equipment[0]}!")
    print(f"The ability of {equipment[0]}:")
    for ability in equipment[1:]:
        print(f"{ability[0]} {ability[1]}")
    print()
    return equipment


def use_equipment(character_dictionary: dict, old_equipment: list, new_equipment: list):
    """
    Use or replace equipment.

    :param character_dictionary: a dictionary of character attributes
    :param old_equipment: a list
    :param new_equipment: a list
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
     items, equipment and debuffs
    :precondition: for old_equipment and new_equipment, index 0 must be a string as equipment name
    :precondition: elements from index 1 must be a tuple (character attribute, integer)

    >>> character_dictionary_1 = {
    ...        "Character_status": {"Level": 1, "HP": 70, "STR": 18, "DEF": 5, "CHR": 5, "SPD": 5, "LUK": 5, "VIS": 2},
    ...        "Equipment": 0}
    >>> old_equipment_1 = [0]
    >>> new_equipment_1 = ["Cloak", ("SPD", 3)]
    >>> use_equipment(character_dictionary_1, old_equipment_1, new_equipment_1)
    <BLANKLINE>
    >>> character_dictionary_1
    {'Character_status': {'Level': 1, 'HP': 70, 'STR': 18, 'DEF': 5, 'CHR': 5, 'SPD': 8, 'LUK': 5, 'VIS': 2}, 'Equipmen\
t': ['Cloak', ('SPD', 3)]}

    >>> character_dictionary_1 = {
    ...        "Character_status": {"Level": 1, "HP": 70, "STR": 18, "DEF": 5, "CHR": 5, "SPD": 8, "LUK": 5, "VIS": 2},
    ...        "Equipment": 0}
    >>> old_equipment_1 = ["Cloak", ("SPD", 3)]
    >>> new_equipment_1 = ["Steel sword", ("STR", 3)]
    >>> use_equipment(character_dictionary_1, old_equipment_1, new_equipment_1)
    <BLANKLINE>
    >>> character_dictionary_1
    {'Character_status': {'Level': 1, 'HP': 70, 'STR': 21, 'DEF': 5, 'CHR': 5, 'SPD': 5, 'LUK': 5, 'VIS': 2}, 'Equipmen\
t': ['Steel sword', ('STR', 3)]}
    """
    if old_equipment != 0:
        for ability in old_equipment[1:]:
            if ability[0] in character_dictionary['Character_status']:
                character_dictionary['Character_status'][ability[0]] -= ability[1]
    
    character_dictionary["Equipment"] = new_equipment
    for ability in new_equipment[1:]:
        if ability[0] in character_dictionary['Character_status']:
            character_dictionary['Character_status'][ability[0]] += ability[1]
    print()
