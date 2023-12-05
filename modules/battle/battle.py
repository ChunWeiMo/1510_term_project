"""
Battle module.
"""
import random
from modules.character import character
from modules.character import items
import itertools


def run_away(character_dictionary):
    chance = 50 + character_dictionary["Character_status"]["SPD"] + character_dictionary["Character_status"]["LUK"] * 2
    random_number = random.randint(1, 100)
    if chance >= random_number >= 1:
        print("Successfully escaped!\n")
        return True
    else:
        print("You failed to escape...prepare to engage in battle!\n")
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
            turn = character_turn(character_dictionary, enemy_appeared, turn)
        else:
            turn = enemy_turn(character_dictionary, enemy_appeared, turn)
    if enemy_appeared["HP"] <= 0:
        is_enemy_killed = enemy_defeated(character_dictionary, enemy_appeared)
    if character_dictionary["Character_status"]["HP"] <= 0:
        return
    return is_enemy_killed


def character_turn(character_dictionary, enemy_appeared, turn):
    if character_dictionary["Character_status"]["STR"] - enemy_appeared["DEF"] <= 0:
        damage = 1
    else:
        damage = character_dictionary["Character_status"]["STR"] - enemy_appeared["DEF"]
    enemy_appeared["HP"] -= damage
    dead = is_enemy_dead(enemy_appeared, damage)
    if not dead:
        speedy(turn, character_dictionary, enemy_appeared, damage)
    turn = "enemy"
    return turn


def is_enemy_dead(enemy_appeared, damage):
    if enemy_appeared["HP"] > 0:
        print(f"\nYou deal {damage} damage to {enemy_appeared['Name']}!\n"
              f"The {enemy_appeared['Name']} has {enemy_appeared['HP']} HP left.\n")
        return False
    else:
        print(f"\nYou deal {damage} damage to {enemy_appeared['Name']}!\n"
              f"The {enemy_appeared['Name']} has 0 HP left.\n")
        return True


def enemy_turn(character_dictionary, enemy_appeared, turn):
    if enemy_appeared["STR"] - character_dictionary["Character_status"]["DEF"] <= 0:
        damage = 1
    else:
        damage = enemy_appeared["STR"] - character_dictionary["Character_status"]["DEF"]
    character_dictionary["Character_status"]["HP"] -= damage
    dead = is_character_dead(character_dictionary, enemy_appeared, damage)
    if not dead:
        speedy(turn, character_dictionary, enemy_appeared, damage)
    turn = "character"
    return turn


def is_character_dead(character_dictionary, enemy_appeared, damage):
    if character_dictionary['Character_status']['HP'] > 0:
        print(f"{enemy_appeared['Name']} dealt {damage} damage to you!\n"
              f"You have {character_dictionary['Character_status']['HP']} HP left.\n")
        return False
    else:
        print(f"{enemy_appeared['Name']} dealt {damage} damage to you!\n"
              f"You have 0 HP left.")
        return True


def enemy_defeated_talk(character_dictionary, enemy_appeared):
    get_loot(character_dictionary, enemy_appeared)
    print("The talk was successful!\n")
    print(f"{enemy_appeared['Name']} is enamoured with you!\n"
          f"You've gained {enemy_appeared['Gold']} gold!\n"
          f"You've gained {enemy_appeared['EXP']} experience!\n"
          f"Your experience is now at {character_dictionary['EXP']}/100!\n")
    if character_dictionary["EXP"] >= 100:
        level_up(character_dictionary)
    return True


def enemy_defeated(character_dictionary, enemy_appeared):
    get_loot(character_dictionary, enemy_appeared)
    print(f"{enemy_appeared['Name']} has been slain!\n"
          f"You've gained {enemy_appeared['Gold']} gold!\n"
          f"You've gained {enemy_appeared['EXP']} experience!\n"
          f"Your experience is now at {character_dictionary['EXP']}/100!\n")
    if character_dictionary["EXP"] >= 100:
        level_up(character_dictionary)
    return True


def get_loot(character_dictionary, enemy_appeared):
    character_dictionary["EXP"] += enemy_appeared["EXP"]
    character_dictionary['Items']['Gold'] += enemy_appeared["Gold"]
    potion_chance(character_dictionary, enemy_appeared)


def potion_chance(character_dictionary, enemy_appeared):
    lucky_number = random.randint(1, 10)
    if lucky_number == 7:
        character_dictionary['Items']['Potions'] += 1
        print(f"{enemy_appeared['Name']} dropped 1 potion!\n")
    else:
        return


def level_up(character_dictionary):
    character_dictionary["Character_status"]["Level"] += 1
    print(f"You leveled up! You are now level {character_dictionary['Character_status']['Level']}\n")
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
        is_enemy_dead(enemy_appeared, damage)
    if turn == "enemy" and enemy_appeared["SPD"] >= character_dictionary["Character_status"]["SPD"] * 2:
        character_dictionary["Character_status"]["HP"] -= damage
        is_character_dead(character_dictionary, enemy_appeared, damage)


def fight_miniboss(character_dictionary, enemy_appeared):
    is_enemy_killed = False
    turn = "character"
    rounds = 0
    while enemy_appeared["HP"] > 0 and character_dictionary["Character_status"]["HP"] > 0:
        if turn == "character":
            can_run = miniboss_menu(character_dictionary, enemy_appeared)
            if not can_run:
                turn = character_turn(character_dictionary, enemy_appeared, turn)
            else:
                break
        else:
            print(f"\nIt is {enemy_appeared['Name']}'s turn!\n")
            turn = miniboss_turn(character_dictionary, enemy_appeared, turn, rounds)
            rounds += 1
    if enemy_appeared["HP"] <= 0:
        is_enemy_killed = enemy_defeated(character_dictionary, enemy_appeared)
    if character_dictionary["Character_status"]["HP"] <= 0:
        return
    return is_enemy_killed


def miniboss_menu(character_dictionary, enemy_appeared):
    try:
        boss_response = int(input("It is currently your turn. What would you like to do?\n"
                                  "[1] Fight\n"
                                  "[2] Use item\n"
                                  "[3] Escape\n"))
    except ValueError:
        print("You must enter 1 or 3.\n")
    else:
        if boss_response < 1 or boss_response > 3:
            print("You must enter 1 or 3.\n")
            miniboss_menu(character_dictionary, enemy_appeared)
        elif boss_response == 1:
            return
        elif boss_response == 2:
            items.use_potion(character_dictionary)
            boss_menu(character_dictionary)
        else:
            can_run = run_away(character_dictionary)
            return can_run


def miniboss_turn(character_dictionary, enemy_appeared, turn, rounds):
    if enemy_appeared["Name"] == "Cerberus":
        [cerberus_turn(character_dictionary, enemy_appeared) for _ in itertools.repeat(None, 3)]
        turn = "character"
    elif enemy_appeared["Name"] == "Oberon":
        turn = oberon_turn(character_dictionary, enemy_appeared, turn, rounds)
    else:
        turn = dracula_turn(character_dictionary, enemy_appeared)
    return turn


def cerberus_turn(character_dictionary, enemy_appeared):
    if character_dictionary["Character_status"]["HP"] > 0:
        if enemy_appeared["STR"] - character_dictionary["Character_status"]["DEF"] <= 0:
            damage = 1
            character_dictionary["Character_status"]["HP"] -= damage
        else:
            damage = enemy_appeared["STR"] - character_dictionary["Character_status"]["DEF"]
            character_dictionary["Character_status"]["HP"] -= damage
            is_character_dead(character_dictionary, enemy_appeared, damage)
    else:
        return


def oberon_turn(character_dictionary, enemy_appeared, turn, rounds):
    if rounds % 3 == 0:
        summon_pixie(enemy_appeared)
    enemy_turn(character_dictionary, enemy_appeared, turn)
    return turn


def summon_pixie(enemy_appeared):
    if enemy_appeared["HP"] + 10 >= 40:
        enemy_appeared["HP"] = 4
    else:
        enemy_appeared["HP"] += 10
    print("Oberon has summoned a High Pixie! The Pixie heals him for 10 HP.\n"
          f"Oberon now has {enemy_appeared['HP']} HP.\n")


def dracula_turn(character_dictionary, enemy_appeared):
    if enemy_appeared["STR"] - character_dictionary["Character_status"]["DEF"] <= 0:
        damage = 1
    else:
        damage = enemy_appeared["STR"] - character_dictionary["Character_status"]["DEF"]
    character_dictionary["Character_status"]["HP"] -= damage
    dead = is_character_dead(character_dictionary, enemy_appeared, damage)
    if not dead:
        cure_hp(enemy_appeared, damage)
        speedy_drac(character_dictionary, enemy_appeared, damage)
    turn = "character"
    return turn


def cure_hp(enemy_appeared, damage):
    if enemy_appeared["HP"] + damage >= 40:
        enemy_appeared["HP"] = 40
    else:
        enemy_appeared["HP"] += damage
    print("Dracula has sucked your blood! He recovered HP.\n"
          f"Dracula now has {enemy_appeared['HP']} HP.\n")


def speedy_drac(character_dictionary, enemy_appeared, damage):
    if enemy_appeared["SPD"] > character_dictionary["Character_status"]["SPD"] * 2:
        dead = is_character_dead(character_dictionary, enemy_appeared, damage)
        if not dead:
            cure_hp(enemy_appeared, damage)
    else:
        return


def fight_final_boss(character_dictionary, enemy_appeared):
    print("\nThe dragon roars loud and ferocious, sending a chill down your spine.\n")
    achieved_goal = False
    turn = "character"
    boss_battle(character_dictionary, enemy_appeared, turn)
    if enemy_appeared["HP"] <= 0:
        enemy_defeated(character_dictionary, enemy_appeared)
        achieved_goal = True
    if character_dictionary["Character_status"]["HP"] <= 0:
        return
    return achieved_goal


def boss_battle(character_dictionary, enemy_appeared, turn):
    while enemy_appeared["HP"] > 0 and character_dictionary["Character_status"]["HP"] > 0:
        if turn == "character":
            if character_dictionary["Debuff"]["Burn"] > 0:
                print(f"You've been burnt! You lose 5 HP.\n"
                      f"You have {character_dictionary['Character_status']['HP']} HP left.\n")
                character_dictionary["Character_status"]["HP"] -= 5
            if character_dictionary["Character_status"]["HP"] > 0:
                boss_menu(character_dictionary)
                turn = character_turn(character_dictionary, enemy_appeared, turn)
            else:
                break
        else:
            print("\nIt is the dragons turn!\n")
            turn = boss_turn(character_dictionary, enemy_appeared, turn)


def boss_menu(character_dictionary):
    try:
        boss_response = int(input("It is currently your turn. What would you like to do?\n"
                                  "[1] Fight\n"
                                  "[2] Use item\n"))
    except ValueError:
        print("\nYou must enter 1 or 2.\n")
    else:
        if boss_response < 1 or boss_response > 2:
            print("\nYou must enter 1 or 2.\n")
            boss_menu(character_dictionary)
        elif boss_response == 1:
            return
        else:
            items.use_potion(character_dictionary)
            boss_menu(character_dictionary)


def boss_turn(character_dictionary, enemy_appeared, turn):
    attack = random.randint(1, 4)
    if attack == 1:
        turn = enemy_turn(character_dictionary, enemy_appeared, turn)
    elif attack == 2:
        turn = boss_fireball(character_dictionary, enemy_appeared)
    elif attack == 3:
        turn = boss_tailwhip(character_dictionary, enemy_appeared)
    else:
        turn = boss_claw_attack(character_dictionary, enemy_appeared)
    return turn


def boss_fireball(character_dictionary, enemy_appeared):
    print("\nThe dragon takes a deep breath, his throat blowing bright orange.\nNext thing you know the room is filled "
          "with flames.\n")
    if enemy_appeared["STR"] - character_dictionary["Character_status"]["DEF"] <= 0:
        damage = 1 + 2
    else:
        damage = enemy_appeared["STR"] - character_dictionary["Character_status"]["DEF"] + 2
    character_dictionary["Character_status"]["HP"] -= damage
    if character_dictionary['Character_status']['HP'] > 0:
        print(f"The {enemy_appeared['Name']} dealt {damage} damage to you!\n"
              f"You have {character_dictionary['Character_status']['HP']} HP left.\n")
        print("You've been burnt by the flames! You will take extra burn damage until the room cools down.\n")
        character_dictionary["Debuff"]["Burn"] = 3
    else:
        print(f"The {enemy_appeared['Name']} dealt {damage} damage to you!\n"
              f"You have 0 HP left.\n")
    turn = "character"
    return turn


def boss_tailwhip(character_dictionary, enemy_appeared):
    print("\nThe dragon turns around and swings his massive tail at you!\n")
    if enemy_appeared["STR"] - character_dictionary["Character_status"]["DEF"] <= 0:
        damage = 1 + 2
    else:
        damage = enemy_appeared["STR"] - character_dictionary["Character_status"]["DEF"] + 2
    character_dictionary["Character_status"]["HP"] -= damage
    if character_dictionary['Character_status']['HP'] > 0:
        print(f"The {enemy_appeared['Name']} dealt {damage} damage to you!\n"
              f"You have {character_dictionary['Character_status']['HP']} HP left.\n")
        stun = random.randint(1, 3)
        if stun == 1:
            print("You've been stunned!\n")
            turn = "enemy"
        else:
            turn = "character"
        return turn
    else:
        print(f"The {enemy_appeared['Name']} dealt {damage} damage to you!\n"
              f"You have 0 HP left.\n")
        return


def boss_claw_attack(character_dictionary, enemy_appeared):
    """
    An attack that ignores player defense.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :precondition:
    :precondition:
    :postcondition: attacks the player for 7 damage and changes the turn back to the player
    :return: a string
    """
    print("\nAn enormous pair of claws swing at you. They are extremely sharp and slice through "
          "even the strongest armour.\n")
    character_dictionary["Character_status"]["HP"] -= enemy_appeared["STR"]
    if character_dictionary['Character_status']['HP'] > 0:
        print(f"The {enemy_appeared['Name']} dealt 7 damage to you!\n"
              f"You have {character_dictionary['Character_status']['HP']} HP left.\n")
    else:
        print(f"The {enemy_appeared['Name']} dealt 7 damage to you!\n"
              f"You have 0 HP left.\n")
    turn = "character"
    return turn
