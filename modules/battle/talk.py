"""Talk module
"""


from modules.battle import enemy_lines
from modules.battle import battle
from modules.battle import enemy
import random


def talk_to_enemy(character_dictionary, enemy_appeared):
    print(f"{enemy_lines.enemy_appeared['Chat']['Question']}")
    response_options = randomizer(enemy_appeared)
    response = get_chat_response(response_options)
    get_reply(response, response_options, character_dictionary, enemy_appeared)


def randomizer(enemy_appeared):
    answer_randomizer = random.randint(1, 3)
    if answer_randomizer == 1:
        response_options = {1: enemy_lines.enemy_appeared['Chat']["Answer 1"],
                            2: enemy_lines.enemy_appeared['Chat']["Answer 2"],
                            3: enemy_lines.enemy_appeared['Chat']["Answer 3"]}
    elif answer_randomizer == 2:
        response_options = {3: enemy_lines.enemy_appeared['Chat']["Answer 1"],
                            1: enemy_lines.enemy_appeared['Chat']["Answer 2"],
                            2: enemy_lines.enemy_appeared['Chat']["Answer 3"]}
    else:
        response_options = {2: enemy_lines.enemy_appeared['Chat']["Answer 1"],
                            3: enemy_lines.enemy_appeared['Chat']["Answer 2"],
                            1: enemy_lines.enemy_appeared['Chat']["Answer 3"]}
    return response_options


def get_chat_response(response_options):
    response = input(f"{response_options[1]}\n{response_options[2]}\n{response_options[3]}")
    return response


def get_reply(response, response_options, character_dictionary, enemy_appeared):
    if response_options[response] == enemy_lines.enemy_appeared['Chat']["Answer 1"]:
        battle.enemy_defeated(character_dictionary, enemy_appeared)
    elif response_options[response] == enemy_lines.enemy_appeared['Chat']["Answer 2"]:
        if character_dictionary["Character_status"]["CHR"] + 5 >= 10:
            battle.enemy_defeated(character_dictionary, enemy_appeared)
        else:
            can_start = False
            battle.fight(character_dictionary, enemy_appeared, can_start)
    else:
        if character_dictionary["Character_status"]["CHR"] + 3 >= 10:
            battle.enemy_defeated(character_dictionary, enemy_appeared)
        else:
            can_start = False
            battle.fight(character_dictionary, enemy_appeared, can_start)
