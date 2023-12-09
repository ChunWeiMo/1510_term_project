"""
Enemy module. This module contains functions related to defining and encountering enemies.
"""
import random
from modules.battle import battle
from modules.battle import talk
from modules.character import items


def enemy() -> dict:
    """
    Create an enemy dictionary.

    :postcondition: creates a dictionary with 4 elements, a dictionary of level 1 enemies, a dictionary of level 2
    enemies, a dictionary of minibosses, and a final boss
    :return: a dictionary of nested dictionaries
    """
    slime = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
    pixie = {"Name": "Pixie", "HP": 6, "STR": 2, "DEF": 1, "SPD": 3, "EXP": 3, "Gold": 1}
    wolf = {"Name": "Wolf", "HP": 15, "STR": 3, "DEF": 1, "SPD": 2, "EXP": 5, "Gold": 1}
    skeleton = {"Name": "Skeleton", "HP": 15, "STR": 2, "DEF": 2, "SPD": 2, "EXP": 3, "Gold": 1}
    ghost = {"Name": "Ghost", "HP": 10, "STR": 2, "DEF": 0, "SPD": 4, "EXP": 5, "Gold": 1}
    golem = {"Name": "Golem", "HP": 20, "STR": 1, "DEF": 5, "SPD": 0, "EXP": 5, "Gold": 1}

    cave_spider = {"Name": "Cave Spider", "HP": 25, "STR": 1, "DEF": 2, "SPD": 5, "EXP": 3, "Gold": 2}
    skeleton_archer = {"Name": "Skeleton Archer", "HP": 20, "STR": 4, "DEF": 0, "SPD": 4, "EXP": 3, "Gold": 2}
    restless_spirit = {"Name": "Restless Spirit", "HP": 30, "STR": 4, "DEF": 1, "SPD": 3, "EXP": 5, "Gold": 2}
    succubus = {"Name": "Succubus", "HP": 20, "STR": 3, "DEF": 1, "SPD": 4, "EXP": 5, "Gold": 2}
    dungeon_maid = {"Name": "Dungeon Maid", "HP": 25, "STR": 3, "DEF": 3, "SPD": 2, "EXP": 3, "Gold": 2}
    gargoyle = {"Name": "Gargoyle", "HP": 40, "STR": 2, "DEF": 6, "SPD": 0, "EXP": 5, "Gold": 2}

    cerberus = {"Name": "Cerberus", "HP": 50, "STR": 5, "DEF": 5, "SPD": 0, "EXP": 8, "Gold": 5}
    oberon = {"Name": "Oberon", "HP": 40, "STR": 4, "DEF": 0, "SPD": 6, "EXP": 8, "Gold": 5}
    dracula = {"Name": "Dracula", "HP": 40, "STR": 5, "DEF": 1, "SPD": 4, "EXP": 8, "Gold": 5}

    dragon = {"Name": "Evil Dragon", "HP": 100, "STR": 7, "DEF": 4, "SPD": 3, "EXP": 10, "Gold": 10}

    enemy_dictionary = {
        "Level 1": {1: slime, 2: pixie, 3: wolf, 4: skeleton, 5: ghost, 6: golem},
        "Level 2": {1: cave_spider, 2: skeleton_archer, 3: restless_spirit, 4: succubus, 5: dungeon_maid, 6: gargoyle},
        "Miniboss": {1: cerberus, 2: oberon, 3: dracula},
        "Final Boss": dragon
    }
    return enemy_dictionary


def select_enemy(character_dictionary: dict, enemy_dictionary: dict) -> dict:
    """
    Select a random enemy for the player to encounter from the level 1 and level 2 enemy dictionaries.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_dictionary: a dictionary of nested dictionaries
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_dictionary is a dictionary with 4 elements, a dictionary of level 1 enemies, a dictionary of
    level 2 enemies, a dictionary of minibosses, and a final boss
    :return: a dictionary of enemy attributes
    """
    if character_dictionary["Character_status"]["Level"] == 1:
        enemy_appeared = enemy_dictionary["Level 1"][random.randint(1, 6)]
    else:
        enemy_appeared = enemy_dictionary["Level 2"][random.randint(1, 6)]
    return enemy_appeared


def ask_user(enemy_appeared: dict) -> int:
    """
    Get input from the player on what they want to do upon encountering an enemy.

    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :postcondition: returns a positive integer between 1 and 4 inclusive depending on what the player has inputted
    :return: a positive integer
    """
    print(f"{enemy_appeared['Name']} appears before you!")
    while True:
        try:
            user_input = int(input("What will you do?\n"
                                   "[1] Battle the monster\n"
                                   "[2] Talk to the monster\n"
                                   "[3] Use item\n"
                                   "[4] Run away\n"))
        except ValueError:
            print("Please enter a number between 1-4.")
        else:
            if user_input > 4 or user_input < 1:
                print("Please enter a number between 1-4.")
                continue
            else:
                return user_input


def battle_talk_escape(character_dictionary: dict, user_input: int, enemy_appeared: dict) -> bool:
    """
    Determines what the player will do when encountering an enemy and returns True if the enemy is defeated.

    :param character_dictionary: a dictionary of character attributes
    :param user_input: a positive integer
    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: user_input is a positive integer between 1 and 4 inclusive
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :postcondition: returns True if the encountered enemy was killed or False if the character has died in the battle
    :return: a boolean value True or False
    """
    is_enemy_killed = False
    if user_input == 1:
        can_start = True
        if (enemy_appeared["Name"] == "Cerberus" or
                enemy_appeared["Name"] == "Oberon" or
                enemy_appeared["Name"] == "Dracula"):
            is_enemy_killed = battle.fight_miniboss(character_dictionary, enemy_appeared)
            return is_enemy_killed
        if enemy_appeared["Name"] == "Evil Dragon":
            achieved_goal = battle.fight_final_boss(character_dictionary, enemy_appeared)
            return achieved_goal
        else:
            is_enemy_killed = battle.fight(character_dictionary, enemy_appeared, can_start)
            return is_enemy_killed
    elif user_input == 2:
        if enemy_appeared["Name"] == "Evil Dragon":
            achieved_goal_talk = talk.talk_to_enemy(character_dictionary, enemy_appeared)
            return achieved_goal_talk
        else:
            is_enemy_killed = talk.talk_to_enemy(character_dictionary, enemy_appeared)
            return is_enemy_killed
    elif user_input == 3:
        items.use_potion(character_dictionary)
        ask_user(enemy_appeared)
    else:
        if enemy_appeared["Name"] == "Evil Dragon":
            print(f"You cannot run away from {enemy_appeared['Name']}!")
            ask_user(enemy_appeared)
        else:
            can_run = battle.run_away(character_dictionary)
            if not can_run:
                can_start = False
                is_enemy_killed = battle.fight(character_dictionary, enemy_appeared, can_start)
            return is_enemy_killed
