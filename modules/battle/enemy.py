"""
Enemy module.
"""
import random
from modules.battle import battle
from modules.battle import talk
from modules.character import items


def enemy():
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

    # special: attack will cause burn for extra 1 dmg
    cerberus = {"Name": "Cerberus", "HP": 50, "STR": 5, "DEF": 5, "SPD": 0, "EXP": 8, "Gold": 5}
    # special: summons 2 pixies every 3 turns
    oberon = {"Name": "Oberon", "HP": 40, "STR": 4, "DEF": 0, "SPD": 6, "EXP": 8, "Gold": 5}
    # special: gains 1 HP after attack
    dracula = {"Name": "Dracula", "HP": 40, "STR": 5, "DEF": 1, "SPD": 4, "EXP": 8, "Gold": 5}

    dragon = {"Name": "Evil Dragon", "HP": 100, "STR": 7, "DEF": 4, "SPD": 3}  # 3 special moves

    enemy_dictionary = {
        "Level 1": {1: slime, 2: pixie, 3: wolf, 4: skeleton, 5: ghost, 6: golem},
        "Level 2": {1: cave_spider, 2: skeleton_archer, 3: restless_spirit, 4: succubus, 5: dungeon_maid, 6: gargoyle},
        "Miniboss": {1: cerberus, 2: oberon, 3: dracula},
        "Final Boss": dragon
    }
    return enemy_dictionary


def select_enemy(character_dictionary, enemy_dictionary):
    if character_dictionary["Character_status"]["Level"] == 1:
        enemy_appeared = enemy_dictionary["Level 1"][random.randint(1, 6)]
    elif character_dictionary["Character_status"]["Level"] == 2:
        enemy_appeared = enemy_dictionary["Level 2"][random.randint(1, 6)]
    else:
        enemy_appeared = enemy_dictionary["Final Boss"]
    return enemy_appeared


def ask_user(enemy_appeared):
    print(f"A {enemy_appeared['Name']} appears before you!")
    user_input = input("What will you do?\n"
                       "[1] Battle the monster\n"
                       "[2] Talk to the monster\n"
                       "[3] Use item\n"
                       "[4] Run away\n")
    return user_input


def battle_talk_escape(character_dictionary, user_input, enemy_appeared):
    is_enemy_killed = False
    if user_input == "1":
        can_start = True
        is_enemy_killed = battle.fight(character_dictionary, enemy_appeared, can_start)
        return is_enemy_killed
    elif user_input == "2":
        if (enemy_appeared["Name"] == "Cerberus" or
                enemy_appeared["Name"] == "Oberon" or
                enemy_appeared["Name"] == "Dracula"):
            is_enemy_killed = talk.talk_to_enemy(character_dictionary, enemy_appeared)
            return is_enemy_killed
        elif enemy_appeared["Name"] == "Evil Dragon":
            achieved_goal_talk = talk.talk_to_enemy(character_dictionary, enemy_appeared)
            return achieved_goal_talk
        else:
            is_enemy_killed = talk.talk_to_enemy(character_dictionary, enemy_appeared)
            return is_enemy_killed
    elif user_input == "3":
        items.use_potion(character_dictionary)
        ask_user(enemy_appeared)
    else:
        can_run = battle.run_away(character_dictionary)
        if not can_run:
            can_start = False
            is_enemy_killed = battle.fight(character_dictionary, enemy_appeared, can_start)
        return is_enemy_killed
