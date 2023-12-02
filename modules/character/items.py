"""
Items module

For:
    -Treasure Chests
    -Monster Loot & Drops
    -Merchants
"""


def use_potion(character_dictionary):
    if character_dictionary["Character_status"]["Level"] == 1:
        max_hp = 100
    elif character_dictionary["Character_status"]["Level"] == 2:
        max_hp = 120
    else:
        max_hp = 150

    if character_dictionary["Items"]["Potions"] > 0:
        response = ask_player_potions(character_dictionary)
        catch_potion_error(response, character_dictionary)
        heal_character(character_dictionary, response, max_hp)
    else:
        print("You have 0 potions to use.")
    return


def ask_player_potions(character_dictionary):
    response = int(input(f"You have {character_dictionary['Items']['Potions']} potions and "
                     f"{character_dictionary['Character_status']['HP']} HP.\n"
                     f"Enter how many potions you would like to use:\n"))
    if response <= 0 or response > character_dictionary['Items']['Potions']:
        print(f"You must enter a number between 1 and {character_dictionary['Items']['Potions']}.")
        ask_player_potions(character_dictionary)
    else:
        return response


def heal_character(character_dictionary, response, max_hp):
    if character_dictionary["Character_status"]["HP"] <= max_hp - response * 20:
        character_dictionary["Character_status"]["HP"] += response * 20
    else:
        character_dictionary["Character_status"]["HP"] = max_hp


def catch_potion_error(response, character_dictionary):
    if response <= 0:
        raise IndexError(f"You must enter a number between 1 and {character_dictionary['Items']['Potions']}.")
