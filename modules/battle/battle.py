"""
Battle module.
"""
import random
from modules.character import character
from modules.character import items
import itertools


def run_away(character_dictionary):
    """
    Determine whether the player can run away from battle.

    :param character_dictionary: a dictionary of character attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :postcondition: returns True if the player can run away from battle and False if the player cannot
    :return: a boolean True or False
    """
    chance = 50 + character_dictionary["Character_status"]["SPD"] + character_dictionary["Character_status"]["LUK"] * 2
    random_number = random.randint(1, 100)
    if chance >= random_number >= 1:
        print("Successfully escaped!\n")
        return True
    else:
        print("You failed to escape...prepare to engage in battle!\n")
        return False


def who_goes_first(character_dictionary, enemy_appeared):
    """
    Determine who goes first in battle.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :postcondition: returns a string of either "character" or "enemy" depending on who goes first
    :return: a string of either "character" or "enemy"
    """
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
    """
    Start battle mode with an enemy.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :param can_start: a boolean True or False
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :precondition: can_start is True if the chance of player starting the battle will be determined by calculation
    :precondition: can_start is False if the enemy will always start the battle
    :postcondition: when fighting a miniboss or regular enemy, upon a successful battle, return True for enemy defeated
    :postcondition: when fighting the final boss, upon a successful battle, return True for goal achieved
    :postcondition: when fighting any enemy, upon an unsuccessful battle, return False for enemy defeated
    :return: a boolean True or False
    """
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
    """
    Attack the enemy during the player's turn.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :param turn: a string of either "character" or "enemy"
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :precondition: turn is a string of either "character" or "enemy" depending on who's turn it is
    :postcondition: calculates how much damage the player deals to the enemy and subtracts it from the enemy's HP
    :postcondition: checks if the enemy is dead and returns True if dead and False if not dead
    :postcondition: if the enemy is not dead, check if the player's speed is double the enemy's speed and if so,
    attack the enemy again
    :postcondition: returns a string of "enemy" setting the turn to the enemy's turn
    :return: a string of either "character" or "enemy"
    """
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
    """
    Check if the enemy is dead.

    :param enemy_appeared: a dictionary of enemy attributes
    :param damage: a positive non-zero integer
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :precondition: damage is a positive non-zero integer representing the amount of damage dealt to the enemy
    :postcondition: prints the amount of damage dealt to the enemy and how much HP the enemy has left
    :postcondition: returns True if the enemy is dead and False if not dead
    :return: a boolean True or False
    """
    if enemy_appeared["HP"] > 0:
        print(f"\nYou deal {damage} damage to {enemy_appeared['Name']}!\n"
              f"The {enemy_appeared['Name']} has {enemy_appeared['HP']} HP left.\n")
        return False
    else:
        print(f"\nYou deal {damage} damage to {enemy_appeared['Name']}!\n"
              f"The {enemy_appeared['Name']} has 0 HP left.\n")
        return True


def enemy_turn(character_dictionary, enemy_appeared, turn):
    """
    Attack the player during the enemy's turn.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :param turn: a string of either "character" or "enemy"
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :precondition: turn is a string of either "character" or "enemy" depending on who's turn it is
    :postcondition: calculates how much damage the enemy deals to the player and subtracts it from the player's HP
    :postcondition: checks if the player is dead and returns True if dead and False if not dead
    :postcondition: if the player is not dead, check if the enemy's speed is double the player's speed and if so,
    attack the player again
    :postcondition: returns a string of "character" setting the turn to the player's turn
    :return: a string of either "character" or "enemy"
    """
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
    """
    Check if the player is dead.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :param damage: a positive non-zero integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :precondition: damage is a positive non-zero integer representing the amount of damage dealt to the player
    :postcondition: prints the amount of damage dealt to the player and how much HP the player has left
    :postcondition: returns True if the player is dead and False if not dead
    :return: a boolean True or False
    """
    if character_dictionary['Character_status']['HP'] > 0:
        print(f"{enemy_appeared['Name']} dealt {damage} damage to you!\n"
              f"You have {character_dictionary['Character_status']['HP']} HP left.\n")
        return False
    else:
        print(f"{enemy_appeared['Name']} dealt {damage} damage to you!\n"
              f"You have 0 HP left.")
        return True


def enemy_defeated_talk(character_dictionary, enemy_appeared):
    """
    Print the results of a successful talk with an enemy.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :postcondition: print the results of a successful talk and return True
    :postcondition: if the player levels up, level up the player
    :return: a boolean True

    >>> character_dictionary = {"Character_status": {"HP": 100, "STR": 10, "DEF": 10, "SPD": 10, "CHR": 10, "LUK": 10},
    ...                         "EXP": 0, "Items": {"Gold": 0, "Potions": 0}, "Equipment": {"Weapon": "Fists",
    ...                         "Armour": "Clothes", "Accessory": "None"}, "Debuffs": []}
    >>> enemy_appeared = {"Name": "Goblin", "HP": 10, "STR": 10, "DEF": 10, "SPD": 10, "EXP": 10, "Gold": 10}
    >>> enemy_defeated_talk(character_dictionary, enemy_appeared)
    The talk was successful!
    Goblin is enamoured with you!
    You've gained 10 gold!
    You've gained 10 experience!
    Your experience is now at 10/100!
    True
    """
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
    """
    Print the results of a successful battle with an enemy.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :postcondition: print the results of a successful battle and return True
    :postcondition: if the player levels up, level up the player
    :return: a boolean True

    >>> character_dictionary = {"Character_status": {"HP": 100, "STR": 10, "DEF": 10, "SPD": 10, "CHR": 10, "LUK": 10},
    ...                         "EXP": 0, "Items": {"Gold": 0, "Potions": 0}, "Equipment": {"Weapon": "Fists",
    ...                         "Armour": "Clothes", "Accessory": "None"}, "Debuffs": []}
    >>> enemy_appeared = {"Name": "Goblin", "HP": 10, "STR": 10, "DEF": 10, "SPD": 10, "EXP": 10, "Gold": 10}
    >>> enemy_defeated(character_dictionary, enemy_appeared)
    Goblin has been slain!
    You've gained 10 gold!
    You've gained 10 experience!
    Your experience is now at 10/100!
    True
    """
    get_loot(character_dictionary, enemy_appeared)
    print(f"{enemy_appeared['Name']} has been slain!\n"
          f"You've gained {enemy_appeared['Gold']} gold!\n"
          f"You've gained {enemy_appeared['EXP']} experience!\n"
          f"Your experience is now at {character_dictionary['EXP']}/100!\n")
    if character_dictionary["EXP"] >= 100:
        level_up(character_dictionary)
    return True


def get_loot(character_dictionary, enemy_appeared):
    """
    Add experience and gold to the character dictionary.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :postcondition: add experience and gold to the character dictionary and add a potion if the player is lucky
    """
    character_dictionary["EXP"] += enemy_appeared["EXP"]
    character_dictionary['Items']['Gold'] += enemy_appeared["Gold"]
    potion_chance(character_dictionary, enemy_appeared)


def potion_chance(character_dictionary, enemy_appeared):
    """
    Add a potion to the character dictionary if the player is lucky.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :postcondition: add a potion to the character dictionary if the player is lucky
    """
    lucky_number = random.randint(1, 10)
    if lucky_number == 7:
        character_dictionary['Items']['Potions'] += 1
        print(f"{enemy_appeared['Name']} dropped 1 potion!\n")
    else:
        return


def level_up(character_dictionary):
    """
    Level up the player.

    :param character_dictionary: a dictionary of character attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :postcondition: level up the player and add 5 attribute points to the character dictionary and reset the player's EXP
    """
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
    """
    Check if the player or enemy can attack again.

    :param turn: a string of either "character" or "enemy"
    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :param damage: a positive non-zero integer
    :precondition: turn is a string of either "character" or "enemy" depending on who's turn it is
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :precondition: damage is a positive non-zero integer representing the amount of damage dealt to the player
    :postcondition: if the player's speed is double the enemy's speed, attack the enemy again and check if the enemy is dead
    :postcondition: if the enemy's speed is double the player's speed, attack the player again and check if the player is dead
    """
    if turn == "character" and character_dictionary["Character_status"]["SPD"] >= enemy_appeared["SPD"] * 2:
        enemy_appeared["HP"] -= damage
        is_enemy_dead(enemy_appeared, damage)
    if turn == "enemy" and enemy_appeared["SPD"] >= character_dictionary["Character_status"]["SPD"] * 2:
        character_dictionary["Character_status"]["HP"] -= damage
        is_character_dead(character_dictionary, enemy_appeared, damage)


def fight_miniboss(character_dictionary, enemy_appeared):
    """
    Start battle mode with a miniboss.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :postcondition: when fighting a miniboss, upon a successful battle, return True for enemy defeated and False if the player is dead
    :return: a boolean True or False

    >>> character_dictionary = {"Character_status": {"HP": 100, "STR": 10, "DEF": 10, "SPD": 10, "CHR": 10, "LUK": 10},
    ...                         "EXP": 0, "Items": {"Gold": 0, "Potions": 0}, "Equipment": {"Weapon": "Fists",
    ...                         "Armour": "Clothes", "Accessory": "None"}, "Debuffs": []}
    >>> enemy_appeared = {"Name": "Cerberus", "HP": 10, "STR": 10, "DEF": 10, "SPD": 10, "EXP": 10, "Gold": 10}
    >>> fight_miniboss(character_dictionary, enemy_appeared)
    Cerberus has been slain!
    You've gained 10 gold!
    You've gained 10 experience!
    Your experience is now at 10/100!
    True
    """
    is_enemy_killed = False
    turn = "character"
    rounds = 1
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
    """
    Display the player's options during battle with a miniboss.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :postcondition: display the player's options during battle with a miniboss
    :postcondition: if the player chooses to use an item, use the item and display the player's options again
    :postcondition: if the player chooses to escape, determine whether the player can run away
    :postcondition: if the input is not between 1-3 inclusive, display the player's options again
    :return: a boolean True or False or None
    """
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
            miniboss_menu(character_dictionary, enemy_appeared)
        else:
            can_run = run_away(character_dictionary)
            return can_run


def miniboss_turn(character_dictionary, enemy_appeared, turn, rounds):
    """
    Attack the player during the miniboss' turn.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :param turn: a string of either "character" or "enemy"
    :param rounds: a positive non-zero integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the randomly selected enemy
    encountered by the player
    :precondition: turn is a string of either "character" or "enemy" depending on who's turn it is
    :precondition: rounds is a positive non-zero integer representing the number of rounds passed
    :postcondition: determines which miniboss the player is fighting and calls the appropriate function
    :postcondition: returns a string of "character" if the next turn will be the player's or "enemy" if the next turn will be the enemy's
    :return: a string of either "character" or None
    """
    if enemy_appeared["Name"] == "Cerberus":
        [cerberus_turn(character_dictionary, enemy_appeared) for _ in itertools.repeat(None, 3)]
        turn = "character"
    elif enemy_appeared["Name"] == "Oberon":
        turn = oberon_turn(character_dictionary, enemy_appeared, turn, rounds)
    else:
        turn = dracula_turn(character_dictionary, enemy_appeared)
    return turn


def cerberus_turn(character_dictionary, enemy_appeared):
    """
    Attack the player during Cerberus' turn.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is Cerberus
    :postcondition: calculates how much damage Cerberus deals to the player and subtracts it from the player's HP
    """
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
    """
    Attack the player during Oberon's turn.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :param turn: a string of either "character" or "enemy"
    :param rounds: a positive non-zero integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of Oberon's attributes
    :precondition: turn is a string "enemy"
    :precondition: rounds is a positive non-zero integer representing the number of rounds passed
    :postcondition: every 3 rounds that have passed Oberon will summon a High Pixie to heal him
    :postcondition: calculates how much damage Oberon deals to the player and subtracts it from the player's HP
    :postcondition: checks if the player is dead and returns True if dead and False if not dead
    :postcondition: if the player is not dead, check if the enemy's speed is double the player's speed and if so,
    attack the player again
    :postcondition: returns a string of "character" setting the turn to the player's turn
    :return: a string of either "character"
    """
    if rounds % 3 == 0:
        summon_pixie(enemy_appeared)
    enemy_turn(character_dictionary, enemy_appeared, turn)
    turn = "character"
    return turn


def summon_pixie(enemy_appeared):
    """
    Summon a High Pixie to heal Oberon.

    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: enemy_appeared is a dictionary of Oberon's attributes
    :postcondition: summon a High Pixie to heal Oberon for 10 HP and print the results
    """
    if enemy_appeared["HP"] + 10 >= 40:
        enemy_appeared["HP"] = 40
    else:
        enemy_appeared["HP"] += 10
    print("Oberon has summoned a High Pixie! The Pixie heals him for 10 HP.\n"
          f"Oberon now has {enemy_appeared['HP']} HP.\n")


def dracula_turn(character_dictionary, enemy_appeared):
    """
    Attack the player during Dracula's turn.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of Dracula's attributes
    :postcondition: calculates how much damage Dracula deals to the player and subtracts it from the player's HP
    :postcondition: checks if the player is dead and returns True if dead and False if not dead
    :postcondition: if the player is not dead, check if the enemy's speed is double the player's speed and if so,
    attack the player again
    :postcondition: returns a string of "character" setting the turn to the player's turn
    :return: a string "character"
    """
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
    """
    Cure Dracula's HP every time he attacks the player.

    :param enemy_appeared: a dictionary of enemy attributes
    :param damage: a positive non-zero integer
    :precondition: enemy_appeared is a dictionary of Dracula's attributes
    :precondition: damage is a positive non-zero integer representing the amount of damage dealt to the player
    :postcondition: cure Dracula's HP every time he attacks the player and print the results
    """
    if enemy_appeared["HP"] + damage >= 40:
        enemy_appeared["HP"] = 40
    else:
        enemy_appeared["HP"] += damage
    print("Dracula has sucked your blood! He recovered HP.\n"
          f"Dracula now has {enemy_appeared['HP']} HP.\n")


def speedy_drac(character_dictionary, enemy_appeared, damage):
    """
    Check if Dracula can attack again.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :param damage: a positive non-zero integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of Dracula's attributes
    :precondition: damage is a positive non-zero integer representing the amount of damage dealt to the player
    :postcondition: if the enemy's speed is double the player's speed, attack the player again and check if the player is dead
    """
    if enemy_appeared["SPD"] > character_dictionary["Character_status"]["SPD"] * 2:
        dead = is_character_dead(character_dictionary, enemy_appeared, damage)
        if not dead:
            cure_hp(enemy_appeared, damage)
    else:
        return


def fight_final_boss(character_dictionary, enemy_appeared):
    """
    Start battle mode with the final boss.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of enemy attributes of the final boss
    :postcondition: when fighting the final boss, upon a successful battle, return True for goal achieved and False if the player is dead
    :return: a boolean True or False
    """
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
    """
    Check whether it is the player's turn or the enemy's turn during the final boss battle.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :param turn: a string of either "character" or "enemy"
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of the final boss' attributes
    :precondition: turn is a string of either "character" or "enemy" depending on who's turn it is
    :postcondition: when fighting the final boss, upon a successful battle, return True for goal achieved and False if the player is dead
    :return: a boolean True or False
    """
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
    """
    Display the player's options during battle with the final boss.

    :param character_dictionary: a dictionary of character attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :postcondition: display the player's options during battle with the final boss
    :postcondition: if the player chooses to use an item, use the item and display the player's options again
    :postcondition: if the input is not between 1-2 inclusive, display the player's options again
    """
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
    """
    Attack the player during the final boss' turn.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :param turn: a string of either "character" or "enemy"
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of the final boss' attributes
    :precondition: turn is a string of either "character" or "enemy" depending on who's turn it is
    :postcondition: determine randomly which attack the final boss will use and return a string of "character" if the next turn will be the player's or "enemy" if the next turn will be the enemy's after the attack
    :return: a string of either "character" or "enemy"
    """
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
    """
    Attack the player with a fireball during the final boss' turn.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of the final boss' attributes
    :postcondition: calculates how much damage the final boss deals to the player and subtracts it from the player's HP
    :postcondition: prints the amount of damage dealt to the player and how much HP the player has left
    :postcondition: checks if the player is dead and prints a message if dead
    :postcondition: add the debuff "Burn" to the character dictionary for 3 rounds
    :postcondition: returns a string of "character" setting the turn to the player's turn
    :return: a string "character"
    """
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
    """
    Attack the player with a tailwhip during the final boss' turn.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of the final boss' attributes
    :postcondition: calculates how much damage the final boss deals to the player and subtracts it from the player's HP
    :postcondition: prints the amount of damage dealt to the player and how much HP the player has left
    :postcondition: checks if the player is dead and prints a message if dead
    :postcondition: stun the player with 30% chance for 1 round and if the character is stunned, return a string of "enemy" setting the turn to the enemy's turn
    :postcondition: returns a string of "character" setting the turn to the player's turn
    :return: a string "character" or "enemy" depending on whether the player is stunned or not
    """
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
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of the final boss' attributes
    :postcondition: calculates how much damage the final boss deals to the player and subtracts it from the player's HP
    :postcondition: prints the amount of damage dealt to the player and how much HP the player has left
    :postcondition: checks if the player is dead and prints a message if dead
    :postcondition: attacks the player for 7 damage and changes the turn back to the player
    :return: a string "character" setting the turn to the player's turn
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
