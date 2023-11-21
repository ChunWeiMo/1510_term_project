"""
Battle module.
"""
import random


def run_away(character_dictionary):
    chance = 50 + character_dictionary["Character_status"]["SPD"] + character_dictionary["Character_status"]["LUK"] * 2
    random_number = random.randint(1, 100)
    if chance >= random_number >= 1:
        return True
    else:
        return False


def fight(character_dictionary, enemy_appeared):
    pass
