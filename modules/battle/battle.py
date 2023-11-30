"""
Battle module.
"""
import random
from modules.character import character


def run_away(character_dictionary):
    chance = 50 + character_dictionary["Character_status"]["SPD"] + character_dictionary["Character_status"]["LUK"] * 2
    random_number = random.randint(1, 100)
    if chance >= random_number >= 1:
        print("Successfully escaped!")
        return True
    else:
        print("You failed to escape...prepare to engage in battle!")
        return False


def who_goes_first(character_dictionary, enemy_appeared):
    if character_dictionary["Character_status"]["SPD"] > enemy_appeared["SPD"]:
        turn = "character"
    elif character_dictionary["Character_status"]["SPD"] == enemy_appeared["SPD"]:
        turn = random.randint(1, 2)
        if turn == 1:
            turn = "character"
        else:
            turn = "enemy"
    else:
        turn = "enemy"
    return turn


def fight(character_dictionary, enemy_appeared, can_start):
    is_enemy_killed = False
    if can_start:
        turn = who_goes_first(character_dictionary, enemy_appeared)
    else:
        turn = "enemy"
    while enemy_appeared["HP"] > 0 and character_dictionary["Character_status"]["HP"] > 0:
        if turn == "character":
            if character_dictionary["Character_status"]["STR"] - enemy_appeared["DEF"] <= 0:
                damage = 1
            else:
                damage = character_dictionary["Character_status"]["STR"] - enemy_appeared["DEF"]
            enemy_appeared["HP"] -= damage
            if enemy_appeared["HP"] > 0:
                print(f"You deal {damage} damage to the {enemy_appeared['Name']}!\n"
                      f"The {enemy_appeared['Name']} has {enemy_appeared['HP']} HP left.")
            else:
                print(f"You deal {damage} damage to the {enemy_appeared['Name']}!\n"
                      f"The {enemy_appeared['Name']} has 0 HP left.")
            speedy(turn, character_dictionary, enemy_appeared, damage)
            turn = "enemy"
        else:
            if enemy_appeared["STR"] - character_dictionary["Character_status"]["DEF"] <= 0:
                damage = 1
            else:
                damage = enemy_appeared["STR"] - character_dictionary["Character_status"]["DEF"]
            character_dictionary["Character_status"]["HP"] -= damage
            if character_dictionary['Character_status']['HP'] > 0:
                print(f"The {enemy_appeared['Name']} dealt {damage} damage to you!\n"
                      f"You now have {character_dictionary['Character_status']['HP']} HP left.")
            else:
                print(f"The {enemy_appeared['Name']} dealt {damage} damage to you!\n"
                      f"You now have 0 HP left.")
            speedy(turn, character_dictionary, enemy_appeared, damage)
            turn = "character"
    if enemy_appeared["HP"] <= 0:
        enemy_defeated(character_dictionary, enemy_appeared)
        is_enemy_killed = True
    if character_dictionary["Character_status"]["HP"] == 0:
        return 
    return is_enemy_killed


def enemy_defeated(character_dictionary, enemy_appeared):
    character_dictionary["EXP"] += enemy_appeared["EXP"]
    character_dictionary['Items']['Gold'] += enemy_appeared["Gold"]
    print(f"{enemy_appeared['Name']} has been slain!\n"
          f"You've gained {enemy_appeared['Gold']} gold!\n"
          f"You've gained {enemy_appeared['EXP']} experience!\n"
          f"Your experience is now at {character_dictionary['EXP']}/100!")
    if character_dictionary["EXP"] >= 100:
        level_up(character_dictionary)


def level_up(character_dictionary):
    character_dictionary["Character_status"]["Level"] += 1
    print(f"You leveled up! You are now level {character_dictionary['Character_status']['Level']}")
    attribute_points = 5
    character_dictionary["EXP"] = 0
    if character_dictionary["Character_status"]["Level"] == 2:
        character_dictionary["Character_status"]["HP"] = 120
    if character_dictionary["Character_status"]["Level"] == 3:
        character_dictionary["Character_status"]["HP"] = 150
    character.add_attribute_points(attribute_points, character_dictionary)


def speedy(turn, character_dictionary, enemy_appeared, damage):
    if turn == "character" and character_dictionary["Character_status"]["SPD"] >= enemy_appeared["SPD"] * 2:
        enemy_appeared["HP"] -= damage
        if enemy_appeared["HP"] > 0:
            print(f"You deal {damage} damage to the {enemy_appeared['Name']}!\n"
                  f"The {enemy_appeared['Name']} has {enemy_appeared['HP']} HP left.")
        else:
            print(f"You deal {damage} damage to the {enemy_appeared['Name']}!\n"
                  f"The {enemy_appeared['Name']} has 0 HP left.")
    if turn == "enemy" and enemy_appeared["SPD"] >= character_dictionary["Character_status"]["SPD"] * 2:
        character_dictionary["Character_status"]["HP"] -= damage
        if character_dictionary['Character_status']['HP'] > 0:
            print(f"The {enemy_appeared['Name']} dealt {damage} damage to you!\n"
                  f"You now have {character_dictionary['Character_status']['HP']} HP left.")
        else:
            print(f"The {enemy_appeared['Name']} dealt {damage} damage to you!\n"
                  f"You now have 0 HP left.")
