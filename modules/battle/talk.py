"""
Talk module
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
    is_enemy_killed = False
    achieved_goal_talk = False
    specific_enemy_lines = get_enemy_lines(enemy_appeared)
    turn = 1
    if (enemy_appeared["Name"] == "Cerberus" or
            enemy_appeared["Name"] == "Oberon" or
            enemy_appeared["Name"] == "Dracula"):
        max_turn = 3
        is_enemy_killed = talk_boss(specific_enemy_lines, enemy_appeared, character_dictionary, turn, max_turn)
    elif enemy_appeared["Name"] == "Evil Dragon":
        max_turn = 5
        achieved_goal_talk = talk_boss(specific_enemy_lines, enemy_appeared, character_dictionary, turn, max_turn)
    else:
        print(f"{enemy_appeared['Name']}: {specific_enemy_lines['Question']}")
        response_options = randomizer(specific_enemy_lines)
        response = get_chat_response(response_options)
        is_enemy_killed = get_reply(response, response_options, character_dictionary,
                                    enemy_appeared, specific_enemy_lines)
    if (enemy_appeared["Name"] == "Cerberus" or
            enemy_appeared["Name"] == "Oberon" or
            enemy_appeared["Name"] == "Dracula"):
        return is_enemy_killed
    elif enemy_appeared["Name"] == "Evil Dragon":
        return achieved_goal_talk
    else:
        return is_enemy_killed


def randomizer(specific_enemy_lines):
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
    is_enemy_killed = False
    check_special_lines(response, response_options, character_dictionary)
    if character_dictionary["Character_status"]["HP"] != 0:
        if response_options[response] == specific_enemy_lines["Answer 1"]:
            print(f"{enemy_appeared['Name']}: {specific_enemy_lines['Reply 1']}\n")
            is_enemy_killed = battle.enemy_defeated_talk(character_dictionary, enemy_appeared)
        elif response_options[response] == specific_enemy_lines["Answer 2"]:
            if character_dictionary["Character_status"]["CHR"] + 5 >= 10:
                print(f"{enemy_appeared['Name']}: {specific_enemy_lines['Reply 2.1']}\n")
                check_special_responses(specific_enemy_lines, character_dictionary)
                is_enemy_killed = battle.enemy_defeated_talk(character_dictionary, enemy_appeared)
            else:
                can_start = False
                print(f"{enemy_appeared['Name']}: {specific_enemy_lines['Reply 2']}\n")
                print(f"You've angered {enemy_appeared['Name']}! Get ready for battle...\n")
                battle.fight(character_dictionary, enemy_appeared, can_start)
        else:
            if character_dictionary["Character_status"]["CHR"] + 3 >= 10:
                print(f"{enemy_appeared['Name']}: {specific_enemy_lines['Reply 3.1']}\n")
                check_special_responses(specific_enemy_lines, character_dictionary)
                is_enemy_killed = battle.enemy_defeated_talk(character_dictionary, enemy_appeared)
            else:
                can_start = False
                print(f"{enemy_appeared['Name']}: {specific_enemy_lines['Reply 3']}\n")
                print(f"You've angered {enemy_appeared['Name']}! Get ready for battle...\n")
                is_enemy_killed = battle.fight(character_dictionary, enemy_appeared, can_start)
    return is_enemy_killed


def check_special_lines(response, response_options, character_dictionary):
    if response_options[response] == "Sure...(-5 HP)" or response_options[response] == "Sure ♥(-5 HP)":
        if character_dictionary["Character_status"]["HP"] > 5:
            character_dictionary["Character_status"]["HP"] -= 5
            print(f"You lost 5 HP. You have {character_dictionary['Character_status']['HP']} HP left.\n")
        else:
            print(f"I only have {character_dictionary['Character_status']['HP']} HP left...\nThis is it for me.\n")
            character_dictionary["Character_status"]["HP"] = 0
    elif response_options[response] == "Ok, if you leave me alone (-10 Gold)":
        if character_dictionary["Items"]["Gold"] >= 10:
            character_dictionary["Items"]["Gold"] -= 10
            print(f"You lost 10 Gold. You have {character_dictionary['Items']['Gold']} gold left.\n")
        else:
            print(f"I only have {character_dictionary['Items']['Gold']} gold left...\nTake it.")
            character_dictionary["Items"]["Gold"] = 0
    elif response_options[response] == "Hmmm if it is the only way. (HP -20)":
        if character_dictionary["Character_status"]["HP"] > 20:
            character_dictionary["Character_status"]["HP"] -= 20
            print(f"You lost 20 HP. You have {character_dictionary['Character_status']['HP']} HP left.\n")
        else:
            print(f"I only have {character_dictionary['Character_status']['HP']} HP left...\nThis is it for me.\n")
            character_dictionary["Character_status"]["HP"] = 0
    else:
        return


def check_special_responses(specific_enemy_lines, character_dictionary):
    if (specific_enemy_lines['Reply 2.1'] == "How's a potion sound?" or
            specific_enemy_lines['Reply 2.1'] == "I don't have any human food or drinks, "
                                                 "but I have this potion I got from a dead adventurer!"):
        character_dictionary["Items"]["Potions"] += 1
        print(f"You got 1 potion! You now have {character_dictionary['Items']['Potions']} potions.\n")
    elif specific_enemy_lines['Reply 3.1'] == "EEEK! Yessir! (+5 Gold)":
        character_dictionary["Items"]["Gold"] += 5
        print(f"You got 5 gold! You now have {character_dictionary['Items']['Gold']} gold.\n")
    else:
        return


def talk_boss(specific_enemy_lines, enemy_appeared, character_dictionary, turn, max_turn):
    passed = True
    is_enemy_killed = False
    while turn <= max_turn:
        if turn == 1:
            question = 'Question 1'
        elif turn == 2:
            question = 'Question 2'
        elif turn == 3:
            question = 'Question 3'
        elif turn == 4:
            question = 'Question 4'
        else:
            question = 'Question 5'
        if not passed:
            break
        else:
            print(f"{enemy_appeared['Name']}: {specific_enemy_lines[question]['Question']}")
            response_options = randomizer_boss(specific_enemy_lines, question)
            response = get_chat_response(response_options)
            passed = get_reply_boss(response, response_options, character_dictionary, enemy_appeared,
                                    specific_enemy_lines, question)
            talk_boss(specific_enemy_lines, enemy_appeared, character_dictionary, turn + 1, max_turn)
    if passed:
        if (enemy_appeared["Name"] == "Cerberus" or
                enemy_appeared["Name"] == "Oberon" or
                enemy_appeared["Name"] == "Dracula"):
            is_enemy_killed = True
            return is_enemy_killed
        elif enemy_appeared["Name"] == "Evil Dragon":
            achieved_goal_talk = True
            return achieved_goal_talk


def randomizer_boss(specific_enemy_lines, question):
    answer_randomizer = random.randint(1, 3)
    if answer_randomizer == 1:
        response_options = {1: specific_enemy_lines[question]["Answer 1"],
                            2: specific_enemy_lines[question]["Answer 2"],
                            3: specific_enemy_lines[question]["Answer 3"]}
    elif answer_randomizer == 2:
        response_options = {3: specific_enemy_lines[question]["Answer 1"],
                            1: specific_enemy_lines[question]["Answer 2"],
                            2: specific_enemy_lines[question]["Answer 3"]}
    else:
        response_options = {2: specific_enemy_lines[question]["Answer 1"],
                            3: specific_enemy_lines[question]["Answer 2"],
                            1: specific_enemy_lines[question]["Answer 3"]}
    return response_options


def get_reply_boss(response, response_options, character_dictionary, enemy_appeared, specific_enemy_lines,
                   question):
    passed = False
    if response_options[response] == specific_enemy_lines[question]["Answer 1"]:
        if character_dictionary["Character_status"]["CHR"] + 2 >= 10:
            print(f"{enemy_appeared['Name']}: {specific_enemy_lines[question]['Reply 1.1']}\n")
            passed = True
        else:
            can_start = False
            print(f"{enemy_appeared['Name']}: {specific_enemy_lines[question]['Reply 1']}\n")
            print(f"You've angered {enemy_appeared['Name']}! Get ready for battle...\n")
            battle.fight(character_dictionary, enemy_appeared, can_start)
    elif response_options[response] == specific_enemy_lines[question]["Answer 2"]:
        if character_dictionary["Character_status"]["CHR"] + 1 >= 10:
            print(f"{enemy_appeared['Name']}: {specific_enemy_lines[question]['Reply 2.1']}\n")
            passed = True
        else:
            can_start = False
            print(f"{enemy_appeared['Name']}: {specific_enemy_lines[question]['Reply 2']}\n")
            print(f"You've angered {enemy_appeared['Name']}! Get ready for battle...\n")
            battle.fight(character_dictionary, enemy_appeared, can_start)
    else:
        if character_dictionary["Character_status"]["CHR"] + 0 >= 10:
            print(f"{enemy_appeared['Name']}: {specific_enemy_lines[question]['Reply 3.1']}\n")
            passed = True
        else:
            can_start = False
            print(f"{enemy_appeared['Name']}: {specific_enemy_lines[question]['Reply 3']}\n")
            print(f"You've angered {enemy_appeared['Name']}! Get ready for battle...\n")
            battle.fight(character_dictionary, enemy_appeared, can_start)
    return passed
