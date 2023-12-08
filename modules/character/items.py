"""
Items module. This module holds functions related to using potions in battle and buying potions from the merchant.
"""


def use_potion(character_dictionary: dict):
    """
    Uses potions if the character has potions in their inventory.

    :param character_dictionary: a dictionary of character attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :postcondition: if the character has a positive number of potions in their inventory, ask the player how many
    potions to use and heals them
    """
    if character_dictionary["Character_status"]["Level"] == 1:
        max_hp = 100
    elif character_dictionary["Character_status"]["Level"] == 2:
        max_hp = 120
    else:
        max_hp = 150

    if character_dictionary["Items"]["Potions"] > 0:
        response = ask_player_potions(character_dictionary)
        heal_character(character_dictionary, response, max_hp)
    else:
        print("\nYou have 0 potions to use.")
    return


def ask_player_potions(character_dictionary):
    """
    Ask the player how many potions they want to use.

    :param character_dictionary: a dictionary of character attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :postcondition: returns a positive integer representing the number of potions the player wants to use
    :return: a positive integer
    """
    while True:
        try:
            response = int(input(f"\nYou have {character_dictionary['Items']['Potions']} potions and "
                                 f"{character_dictionary['Character_status']['HP']} HP.\n"
                                 f"Enter how many potions you would like to use:\n"))
        except ValueError:
            print("\nPlease enter the amount of potions as a number.")
        else:
            if response < 0 or response > character_dictionary['Items']['Potions']:
                print(f"\nYou must enter a number between 0 and {character_dictionary['Items']['Potions']}.")
                continue
            return response


def heal_character(character_dictionary, response, max_hp):
    """
    Use potions to heal character HP.

    :param character_dictionary: a dictionary of character attributes
    :param response: a positive integer
    :param max_hp: a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: response is a positive integer representing how many potions the player wants to use
    :precondition: max_hp is a positive integer representing the character's max HP depending on their level
    :postcondition: updates character HP in character dictionary according to how many potions were used
    """
    if character_dictionary["Character_status"]["HP"] <= max_hp - response * 20:
        character_dictionary["Character_status"]["HP"] += response * 20
    else:
        character_dictionary["Character_status"]["HP"] = max_hp
    character_dictionary['Items']['Potions'] -= response
    print(f"\nYour HP is now {character_dictionary['Character_status']['HP']} and you have "
          f"{character_dictionary['Items']['Potions']} potions left.")


def merchant(character_dictionary):
    """
     Select what to do when the player meets a merchant.

    :param character_dictionary: a dictionary of character attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :postcondition: if you input 1, you will enter the buy menu, 2, you will enter battle with the merchant, and 3
    you will leave the encounter
    """
    print("\nMerchant: Oh! What are you doing here? You must be a hero!\nCome check out my humble store!")
    while True:
        try:
            response = int(input("What do you want to do?\n"
                                 "[1] Buy\n"
                                 "[2] Battle\n"
                                 "[3] Leave\n"))
        except ValueError:
            print("\nPlease enter a number from 1-3.")
        else:
            if response > 3 or response < 1:
                print("\nPlease enter a number from 1-3.")
                continue
            elif response == 1:
                buy(character_dictionary)
                break
            elif response == 2:
                battle_merchant(character_dictionary)
                break
            else:
                leave_merchant()
                break


def buy(character_dictionary):
    """
    Select how many potions the player wants to buy from the merchant.

    :param character_dictionary: a dictionary of character attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :postcondition: if the player has the necessary gold, inputting 1 will purchase 1 potion, 2 will purchase 5
    potions, 3 will purchase 10 potions, and 4 will let you stop talking to the merchant
    """
    print(f"\nMerchant: Welcome!\n"
          f"Merchant: You currently have {character_dictionary['Items']['Gold']} gold.")
    while True:
        try:
            buy_response = int(input("Merchant: What would you like to buy?\n"
                                     "[1] Potion x1 -----10 Gold\n"
                                     "[2] Potion x5 -----45 Gold\n"
                                     "[3] Potion x10 ----90 Gold\n"
                                     "[4] Leave\n"))
        except ValueError:
            print("\nPlease enter a number from 1-4.")
        else:
            if buy_response > 4 or buy_response < 1:
                print("\nPlease enter a number from 1-4.")
                continue
            elif buy_response == 1:
                potions = 1
                check_gold(character_dictionary, potions)
                break
            elif buy_response == 2:
                potions = 5
                check_gold(character_dictionary, potions)
                break
            elif buy_response == 3:
                potions = 10
                check_gold(character_dictionary, potions)
                break
            else:
                leave_merchant()
                break


def check_gold(character_dictionary, potions):
    """
    Purchases potions if character has enough gold.

    :param character_dictionary: a dictionary of character attributes
    :param potions: a positive non-zero integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: potions is a positive non-zero integer representing the number of potions the character wants to buy
    :postcondition: if the character has enough gold to buy the potions, the potions will be added to the character's
    inventory and the corresponding amount of gold will be deducted from the player's inventory
    """
    if potions == 1:
        gold_needed = 10
    elif potions == 5:
        gold_needed = 45
    else:
        gold_needed = 90
    if character_dictionary['Items']['Gold'] >= gold_needed:
        character_dictionary['Items']['Potions'] += potions
        character_dictionary['Items']['Gold'] -= gold_needed
        print("\nMerchant: Thank you for your patronage! Come again!")
    else:
        print("\nMerchant: You don't have enough gold! Maybe come back later when you have enough.")
        leave_merchant()


def battle_merchant(character_dictionary):
    """
    Starts battle with the merchant.
    
    :param character_dictionary: a dictionary of character attributes
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience, 
    items, equipment and debuffs
    :postcondition: simulates a battle with the merchant and returns to the main function if the character's HP reaches
    zero
    """
    print("\nMerchant: What! you're trying to rob me?!\nMerchant: Hmph, who do you think I am! "
          "I stay in the dungeon farming for "
          "gold day in an day out.\nMerchant: You cannot defeat me!\n")
    merchant_stats = {"Level": 9999, "HP": 9999, "STR": 50, "DEF": 50, "SPD": 1}
    turn = "merchant"
    while merchant_stats["HP"] > 0 and character_dictionary["Character_status"]["HP"] > 0:
        if turn == "character":
            if character_dictionary["Character_status"]["STR"] - merchant_stats["DEF"] <= 0:
                damage = 1
            else:
                damage = character_dictionary["Character_status"]["STR"] - merchant_stats["DEF"]
            merchant_stats["HP"] -= damage
            print(f"You deal {damage} damage to Merchant!\n"
                  f"Merchant has {merchant_stats['HP']} HP left.")
            turn = "merchant"
        else:
            if merchant_stats["STR"] - character_dictionary["Character_status"]["DEF"] <= 0:
                damage = 1
            else:
                damage = merchant_stats["STR"] - character_dictionary["Character_status"]["DEF"]
            character_dictionary["Character_status"]["HP"] -= damage
            if character_dictionary['Character_status']['HP'] > 0:
                print(f"Merchant dealt {damage} damage to you!\n"
                      f"You have {character_dictionary['Character_status']['HP']} HP left.")
            else:
                print(f"Merchant dealt {damage} damage to you!\n"
                      f"You now have 0 HP left.")
            turn = "character"
    if character_dictionary["Character_status"]["HP"] == 0:
        return


def leave_merchant():
    """
    Prints merchant line after player finishes interacting with the Merchant.

    :postcondition: prints the merchant's goodbye line
    """
    print("\nMerchant: Thanks for stopping by!")
