"""Talk module

To Do:
-create enemy_defeated but for talk only -no enemy slain dialogue
-print enemy replies

"""

from modules.battle import enemy_lines
from modules.battle import battle
import random


def get_enemy_lines(enemy_appeared):
    enemy_lines_dictionary = enemy_lines.enemy_lines()
    if enemy_appeared["Name"] == "Slime":
        specific_enemy_lines = enemy_lines_dictionary["Level 1"][0]
    elif enemy_appeared["Name"] == "Pixie":
        specific_enemy_lines = enemy_lines_dictionary["Level 1"][1]
    elif enemy_appeared["Name"] == "Wolf":
        specific_enemy_lines = enemy_lines_dictionary["Level 1"][2]
    elif enemy_appeared["Name"] == "Skeleton":
        specific_enemy_lines = enemy_lines_dictionary["Level 1"][3]
    elif enemy_appeared["Name"] == "Ghost":
        specific_enemy_lines = enemy_lines_dictionary["Level 1"][4]
    elif enemy_appeared["Name"] == "Golem":
        specific_enemy_lines = enemy_lines_dictionary["Level 1"][5]
    elif enemy_appeared["Name"] == "Cave Spider":
        specific_enemy_lines = enemy_lines_dictionary["Level 2"][0]
    elif enemy_appeared["Name"] == "Skeleton Archer":
        specific_enemy_lines = enemy_lines_dictionary["Level 2"][1]
    elif enemy_appeared["Name"] == "Restless Spirit":
        specific_enemy_lines = enemy_lines_dictionary["Level 2"][2]
    elif enemy_appeared["Name"] == "Succubus":
        specific_enemy_lines = enemy_lines_dictionary["Level 2"][3]
    elif enemy_appeared["Name"] == "Dungeon Maid":
        specific_enemy_lines = enemy_lines_dictionary["Level 2"][4]
    elif enemy_appeared["Name"] == "Gargoyle":
        specific_enemy_lines = enemy_lines_dictionary["Level 2"][5]
    elif enemy_appeared["Name"] == "Cerberus":
        specific_enemy_lines = enemy_lines_dictionary["Miniboss"][0]
    elif enemy_appeared["Name"] == "Oberon":
        specific_enemy_lines = enemy_lines_dictionary["Miniboss"][1]
    elif enemy_appeared["Name"] == "Dracula":
        specific_enemy_lines = enemy_lines_dictionary["Miniboss"][2]
    else:
        specific_enemy_lines = enemy_lines_dictionary["Final Boss"]
    return specific_enemy_lines


def talk_to_enemy(character_dictionary, enemy_appeared):
    specific_enemy_lines = get_enemy_lines(enemy_appeared)
    print(f"{specific_enemy_lines['Question']}")
    response_options = randomizer(enemy_appeared, specific_enemy_lines)
    response = get_chat_response(response_options)
    get_reply(response, response_options, character_dictionary, enemy_appeared, specific_enemy_lines)


def randomizer(enemy_appeared, specific_enemy_lines):
    answer_randomizer = random.randint(1, 3)
    if answer_randomizer == 1:
        response_options = {1: specific_enemy_lines["Answer 1"],
                            2: specific_enemy_lines["Answer 2"],
                            3: specific_enemy_lines["Answer 3"]}
    elif answer_randomizer == 2:
        response_options = {3: specific_enemy_lines["Answer 1"],
                            1: specific_enemy_lines["Answer 2"],
                            2: specific_enemy_lines["Answer 3"]}
    else:
        response_options = {2: specific_enemy_lines["Answer 1"],
                            3: specific_enemy_lines["Answer 2"],
                            1: specific_enemy_lines["Answer 3"]}
    return response_options


def get_chat_response(response_options):
    response = int(input(f"[1]{response_options[1]}\n[2]{response_options[2]}\n[3]{response_options[3]}\n"))
    return response


def get_reply(response, response_options, character_dictionary, enemy_appeared, specific_enemy_lines):
    if response_options[response] == specific_enemy_lines["Answer 1"]:
        print("The talk was successful!\n")
        battle.enemy_defeated(character_dictionary, enemy_appeared)
    elif response_options[response] == specific_enemy_lines["Answer 2"]:
        if character_dictionary["Character_status"]["CHR"] + 5 >= 10:
            print("The talk was successful!\n")
            battle.enemy_defeated(character_dictionary, enemy_appeared)
        else:
            can_start = False
            print("You've angered the monster! Get ready for battle...\n")
            battle.fight(character_dictionary, enemy_appeared, can_start)
    else:
        if character_dictionary["Character_status"]["CHR"] + 3 >= 10:
            print("The talk was successful!\n")
            battle.enemy_defeated(character_dictionary, enemy_appeared)
        else:
            can_start = False
            print("You've angered the monster! Get ready for battle...\n")
            battle.fight(character_dictionary, enemy_appeared, can_start)
