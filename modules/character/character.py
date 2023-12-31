"""
Character module.
"""
from modules.exploration import story_lines


def make_character() -> dict:
    """
    Create the base character.

    :postcondition: create a base character and asks the user to add attribute points
    :postcondition: returns a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :return: a dictionary of character attributes
    """
    character_stats = {"Level": 1, "HP": 100, "STR": 1,
                       "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}
    character_name = create_name()
    print(story_lines.help_lines["character stats"])
    character_dictionary = {"Character_status": character_stats,
                            "Name": character_name,
                            "X-coordinate": 0,
                            "Y-coordinate": 0,
                            "EXP": 0,
                            "Items": {"Gold": 0, "Potions": 0},
                            "Equipment": 0,
                            "Debuff": {"Burn": 0}
                            }
    attribute_points = 10
    add_attribute_points(attribute_points, character_dictionary)
    return character_dictionary


def create_name() -> str:
    """
    Names your character.

    :postcondition: saves a name of the player's choosing, consisting of any unicode character, to the character
    dictionary and prints a greeting to the player
    :return: a string of unicode characters
    """
    character_name = input("Enter your name (Max 10 letters long):\n")
    if len(character_name) == 0 or len(character_name) > 10:
        print("Character name must be between 1-10 characters long.")
        create_name()
    else:
        print(f"\nWelcome {character_name}!\n")
        return character_name


def add_attribute_points(attribute_points: int, character_dictionary: dict):
    """
    Adds attribute points to the character dictionary.

    :param attribute_points: an integer
    :param character_dictionary: a dictionary of character attributes
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :postcondition: adds attribute points to the character dictionary as specifier by the player and prints out the
    character status after all attribute points are used
    """
    while attribute_points > 0:
        try:
            player_point_input = int(input(f"Distribute your attribute points now. You have "
                                           f"{attribute_points} points left "
                                           f"to use.\nWhich attribute would you like to increase?\n"
                                           f"[1] STR\n[2] DEF\n[3] "
                                           f"CHR\n[4] SPD\n[5] LUK\n"))
        except ValueError:
            print("\nPlease enter a number from 1-5.\n")
        else:
            if player_point_input > 5 or player_point_input < 1:
                print("Please enter a number from 1-5.\n")
                continue
            elif player_point_input == 1:
                character_dictionary["Character_status"]["STR"] += 1
                attribute_points -= 1
            elif player_point_input == 2:
                character_dictionary["Character_status"]["DEF"] += 1
                attribute_points -= 1
            elif player_point_input == 3:
                character_dictionary["Character_status"]["CHR"] += 1
                attribute_points -= 1
            elif player_point_input == 4:
                character_dictionary["Character_status"]["SPD"] += 1
                attribute_points -= 1
            else:
                character_dictionary["Character_status"]["LUK"] += 1
                attribute_points -= 1
    print(f"Your stats are: {character_dictionary['Character_status']}\n")
