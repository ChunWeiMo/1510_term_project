"""
Battle module.
"""
import random
import character


def run_away(character_dictionary):
    chance = 50 + character_dictionary["Character_status"]["SPD"] + character_dictionary["Character_status"]["LUK"] * 2
    random_number = random.randint(1, 100)
    if chance >= random_number >= 1:
        return True
    else:
        return False


def who_goes_first(character_dictionary, enemy_appeared):
    if character_dictionary["Character_status"]["SPD"] > enemy_appeared["SPD"]:
        first_turn = "character"
    elif character_dictionary["Character_status"]["SPD"] == enemy_appeared["SPD"]:
        first_turn = random.randint(1, 2)
        if first_turn == 1:
            first_turn = "character"
        else:
            first_turn = "enemy"
    else:
        first_turn = "enemy"
    return first_turn


def fight(character_dictionary, enemy_appeared, can_start):
    if can_start:
        first_turn = who_goes_first(character_dictionary, enemy_appeared)
    else:
        first_turn = "enemy"
    while enemy_appeared["HP"] > 0 and character_dictionary["Character_status"]["HP"] > 0:
        if first_turn == "character":
            if character_dictionary["Character_status"]["STR"] - enemy_appeared["DEF"] <= 0:
                damage_to_enemy = 1
            else:
                damage_to_enemy = character_dictionary["Character_status"]["STR"] - enemy_appeared["DEF"]
            enemy_appeared["HP"] -= damage_to_enemy
            if enemy_appeared["HP"] > 0:
                print(f"You deal {damage_to_enemy} damage to the {enemy_appeared['Name']}!\n"
                      f"The {enemy_appeared['Name']} has {enemy_appeared['HP']} HP left.")
            else:
                print(f"You deal {damage_to_enemy} damage to the {enemy_appeared['Name']}!\n"
                      f"The {enemy_appeared['Name']} has 0 HP left.")
            if character_dictionary["Character_status"]["SPD"] >= enemy_appeared["SPD"] * 2:
                enemy_appeared["HP"] -= damage_to_enemy
                if enemy_appeared["HP"] > 0:
                    print(f"You deal {damage_to_enemy} damage to the {enemy_appeared['Name']}!\n"
                          f"The {enemy_appeared['Name']} has {enemy_appeared['HP']} HP left.")
                else:
                    print(f"You deal {damage_to_enemy} damage to the {enemy_appeared['Name']}!\n"
                          f"The {enemy_appeared['Name']} has 0 HP left.")
            first_turn = "enemy"
        else:
            if enemy_appeared["STR"] - character_dictionary["Character_status"]["DEF"] <= 0:
                damage_to_character = 1
            else:
                damage_to_character = enemy_appeared["STR"] - character_dictionary["Character_status"]["DEF"]
            character_dictionary["Character_status"]["HP"] -= damage_to_character
            if character_dictionary['Character_status']['HP'] > 0:
                print(f"The {enemy_appeared['Name']} dealt {damage_to_character} damage to you!\n"
                      f"You now have {character_dictionary['Character_status']['HP']} HP left.")
            else:
                print(f"The {enemy_appeared['Name']} dealt {damage_to_character} damage to you!\n"
                      f"You now have 0 HP left.")
            if enemy_appeared["SPD"] >= character_dictionary["Character_status"]["SPD"] * 2:
                character_dictionary["Character_status"]["HP"] -= damage_to_character
                if character_dictionary['Character_status']['HP'] > 0:
                    print(f"The {enemy_appeared['Name']} dealt {damage_to_character} damage to you!\n"
                          f"You now have {character_dictionary['Character_status']['HP']} HP left.")
                else:
                    print(f"The {enemy_appeared['Name']} dealt {damage_to_character} damage to you!\n"
                          f"You now have 0 HP left.")
            first_turn = "character"
    if enemy_appeared["HP"] <= 0:
        character_dictionary["EXP"] += enemy_appeared["EXP"]
        print(f"{enemy_appeared['Name']} has been slain!\n"
              f"You've gained {character_dictionary['Items']['Gold']} gold!\n"
              f"You've gained {enemy_appeared['EXP']} experience!\n"
              f"Your experience is now at {character_dictionary['EXP']}/100!")
        if character_dictionary["EXP"] >= 100:
            character_dictionary["Character_status"]["Level"] += 1
            print(f"You leveled up! You are now level {character_dictionary['Character_status']['Level']}")
            attribute_points = 5
            character_dictionary["EXP"] = 0
            if character_dictionary["Character_status"]["Level"] == 2:
                character_dictionary["Character_status"]["HP"] = 120
            if character_dictionary["Character_status"]["Level"] == 3:
                character_dictionary["Character_status"]["HP"] = 150
            character.add_attribute_points(attribute_points, character_dictionary)
    if character_dictionary["Character_status"]["HP"] == 0:
        return
