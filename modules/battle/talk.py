"""
Talk module
"""

from modules.battle import enemy_lines
from modules.battle import battle
import random


def get_enemy_lines(enemy_appeared: dict) -> dict:
    """
    Get the chat options for a specific enemy.

    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :postcondition: retrieve a dictionary of talk lines for a specified enemy where the key is a string representing
     the question or response number and the value is a string representing the line
    :return: a dictionary of keys and values of strings

    >>> enemy_appeared = {"Name": "Slime"}
    >>> get_enemy_lines(enemy_appeared)
    {'Question': 'Plip plop plip plop~~', 'Answer 1': '*Pat it*', 'Answer 2': '*Squeeze it*', 'Answer 3': '*kick it*', \
'Reply 1': 'Pliippp! (it looks happy)', 'Reply 2': 'PLIPP! (battle)', 'Reply 2.1': 'Pliiiipppp~ (it looks content)', 'R\
eply 3': 'GRRrr (battle)', 'Reply 3.1': 'plip..(it looks sad and scared)'}
    """
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


def talk_to_enemy(character_dictionary: dict, enemy_appeared: dict) -> bool:
    """
    Start talk mode with an enemy.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :postcondition: when talking to a miniboss or regular enemy, upon a successful chat, return True for enemy defeated
    :postcondition: when talking to the final boss, upon a successful chat, return True for goal achieved
    :postcondition: when talking to any enemy, upon an unsuccessful chat, return False for enemy defeated
    and head into battle
    :return: a boolean True or False
    """
    specific_enemy_lines = get_enemy_lines(enemy_appeared)
    turn = 1
    if (enemy_appeared["Name"] == "Cerberus" or
            enemy_appeared["Name"] == "Oberon" or
            enemy_appeared["Name"] == "Dracula"):
        max_turn = 3
        is_enemy_killed = talk_boss(specific_enemy_lines, enemy_appeared, character_dictionary, turn, max_turn)
        return is_enemy_killed
    elif enemy_appeared["Name"] == "Evil Dragon":
        max_turn = 5
        achieved_goal_talk = talk_boss(specific_enemy_lines, enemy_appeared, character_dictionary, turn, max_turn)
        return achieved_goal_talk
    else:
        print(f"{enemy_appeared['Name']}: {specific_enemy_lines['Question']}")
        response_options = randomizer(specific_enemy_lines)
        response = get_chat_response(response_options)
        is_enemy_killed = get_reply(response, response_options, character_dictionary, enemy_appeared,
                                    specific_enemy_lines)
        return is_enemy_killed


def randomizer(specific_enemy_lines: dict) -> dict:
    """
    Generates a random sequence of answers from each enemy's specific lines.

    :param specific_enemy_lines: a dictionary of keys and values of strings
    :precondition: specific_enemy_lines is a dictionary of talk lines for a specified enemy where the key is a string
    representing the question or response number and the value is a string representing the line
    :postcondition: generates a dictionary with answers for a specific enemy in a randomized order with
    the key being an integer and the value being a string
    :return: a dictionary of enemy responses
    """
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


def get_chat_response(response_options: dict) -> int:
    """
    Ask the player to input their response to an enemy's question.

    :param response_options: a dictionary of enemy responses
    :precondition: response_options is a dictionary with answers for a specific enemy in a randomized order with
    the key being an integer and the value being a string
    :postcondition: returns a positive non-zero integer between 1-3 inclusive
    :postcondition: prints an error message if the input is not with the range or not an integer
    :return: a positive non-zero integer
    """
    while True:
        try:
            response = int(input(f"[1] {response_options[1]}\n[2] {response_options[2]}\n[3] {response_options[3]}\n"))
        except ValueError:
            print("\nYou must enter an integer between 1 - 3.\n")
        else:
            if response < 1 or response > 3:
                print("\nYou must enter an integer between 1 - 3.\n")
                continue
            return response


def get_reply(response: int, response_options: dict, character_dictionary: dict, enemy_appeared: dict,
              specific_enemy_lines: dict) -> bool:
    """
    Print the enemy's reply to the player's response.

    :param response: a positive non-zero integer
    :param response_options: a dictionary of enemy responses
    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :param specific_enemy_lines: a dictionary of keys and values of strings
    :precondition: response is a positive non-zero integer between 1-3 inclusive
    :precondition: response_options is a dictionary with answers for a specific enemy in a randomized order with
    the key being an integer and the value being a string
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :precondition: specific_enemy_lines is a dictionary of talk lines for a specified enemy where the key is a string
    representing the question or response number and the value is a string representing the line
    :postcondition: prints the enemy reply to the response of the player and returns True if the talk was successful
    :postcondition: if the talk was unsuccessful, enter battle and return True if the battle was won
    :return: a boolean True or False
    """
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


def check_special_lines(response: int, response_options: dict, character_dictionary: dict):
    """
    Check to see if there are any special answers that affect the character dictionary.

    :param response: a positive non-zero integer
    :param response_options: a dictionary of enemy responses
    :param character_dictionary: a dictionary of character attributes
    :precondition: response is a positive non-zero integer between 1-3 inclusive
    :precondition: response_options is a dictionary with answers for a specific enemy in a randomized order with
    the key being an integer and the value being a string
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :postcondition: if the response is a special response, update the character dictionary
    """
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


def check_special_responses(specific_enemy_lines: dict, character_dictionary: dict):
    """
    Check to see if there are any special replies that affect the character dictionary.

    :param specific_enemy_lines: a dictionary of keys and values of strings
    :param character_dictionary: a dictionary of character attributes
    :precondition: specific_enemy_lines is a dictionary of talk lines for a specified enemy where the key is a string
    representing the question or response number and the value is a string representing the line
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :postcondition: if the reply is a special reply, update the character dictionary
    """
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


def talk_boss(specific_enemy_lines: dict, enemy_appeared: dict, character_dictionary: dict, turn: int,
              max_turn: int) -> bool:
    """
    Start talk mode with a miniboss or final boss.

    :param specific_enemy_lines: a dictionary of keys and values of strings
    :param enemy_appeared: a dictionary of enemy attributes
    :param character_dictionary: a dictionary of character attributes
    :param turn: a positive non-zero integer
    :param max_turn: a positive non-zero integer
    :precondition: specific_enemy_lines is a dictionary of talk lines for a specified enemy where the key is a string
    representing the question or response number and the value is a string representing the line
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: turn is a positive non-zero integer between 1-5 inclusive
    :precondition: max_turn is 3 for mini boss and 5 for final boss
    :postcondition: when talking to a miniboss or boss, upon a successful reply, return True and increase turn by 1
    :postcondition: when talking to the final boss, upon a successful chat 5 times, return True for goal achieved
    :postcondition: when talking to a miniboss, upon a successful chat 3 times, return True for enemy defeated
    :postcondition: when talking to a miniboss or final boss, upon an unsuccessful chat, return False and head into battle
    :return: a boolean True or False
    """
    passed = True
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
            turn += 1
    if passed:
        if (enemy_appeared["Name"] == "Cerberus" or
                enemy_appeared["Name"] == "Oberon" or
                enemy_appeared["Name"] == "Dracula"):
            is_enemy_killed = battle.enemy_defeated_talk(character_dictionary, enemy_appeared)
            return is_enemy_killed
        elif enemy_appeared["Name"] == "Evil Dragon":
            achieved_goal_talk = True
            return achieved_goal_talk


def randomizer_boss(specific_enemy_lines: dict, question: str) -> dict:
    """
    Generates a random sequence of answers from each boss' specific lines.

    :param specific_enemy_lines: a dictionary of keys and values of strings
    :param question: a string representing the question number
    :precondition: specific_enemy_lines is a dictionary of talk lines for a specified enemy where the key is a string
    representing the question or response number and the value is a string representing the line
    :precondition: question is a string representing the question number
    :postcondition: generates a dictionary with answers for a specific enemy in a randomized order with
    the key being an integer and the value being a string
    :return: a dictionary of enemy responses
    """
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


def get_reply_boss(response: int, response_options: dict, character_dictionary: dict, enemy_appeared: dict,
                   specific_enemy_lines: dict, question: str) -> bool:
    """
    Print the boss' reply to the player's response.

    :param response: a positive non-zero integer
    :param response_options: a dictionary of enemy responses
    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :param specific_enemy_lines: a dictionary of keys and values of strings
    :param question: a string representing the question number
    :precondition: response is a positive non-zero integer between 1-3 inclusive
    :precondition: response_options is a dictionary with answers for a specific enemy in a randomized order with
    the key being an integer and the value being a string
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :precondition: specific_enemy_lines is a dictionary of talk lines for a specified enemy where the key is a string
    representing the question or response number and the value is a string representing the line
    :precondition: question is a string representing the question number
    :postcondition: prints the enemy reply to the response of the player and returns True if the talk was successful
    :postcondition: if the talk was unsuccessful, enter battle and return True if the battle was won
    :return: a boolean True or False
    """
    passed = False
    if enemy_appeared["Name"] == "Evil Dragon":
        battle_type = battle.fight_final_boss
    else:
        battle_type = battle.fight_miniboss

    if response_options[response] == specific_enemy_lines[question]["Answer 1"]:
        if character_dictionary["Character_status"]["CHR"] + 2 >= 10:
            print(f"{enemy_appeared['Name']}: {specific_enemy_lines[question]['Reply 1.1']}\n")
            passed = True
        else:
            print(f"{enemy_appeared['Name']}: {specific_enemy_lines[question]['Reply 1']}\n")
            print(f"You've angered {enemy_appeared['Name']}! Get ready for battle...\n")
            battle_type(character_dictionary, enemy_appeared)
    elif response_options[response] == specific_enemy_lines[question]["Answer 2"]:
        if character_dictionary["Character_status"]["CHR"] + 1 >= 10:
            print(f"{enemy_appeared['Name']}: {specific_enemy_lines[question]['Reply 2.1']}\n")
            passed = True
        else:
            print(f"{enemy_appeared['Name']}: {specific_enemy_lines[question]['Reply 2']}\n")
            print(f"You've angered {enemy_appeared['Name']}! Get ready for battle...\n")
            battle_type(character_dictionary, enemy_appeared)
    else:
        if character_dictionary["Character_status"]["CHR"] + 0 >= 10:
            print(f"{enemy_appeared['Name']}: {specific_enemy_lines[question]['Reply 3.1']}\n")
            passed = True
        else:
            print(f"{enemy_appeared['Name']}: {specific_enemy_lines[question]['Reply 3']}\n")
            print(f"You've angered {enemy_appeared['Name']}! Get ready for battle...\n")
            battle_type(character_dictionary, enemy_appeared)
    return passed
