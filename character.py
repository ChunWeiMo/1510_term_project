"""
Character module.
"""
import map
import random
import story_lines


def make_character():
    character_stats = {"Level": 1, "HP": 100, "STR": 1,
                       "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1}
    print(story_lines.help_lines["character stats"])
    character_dictionary = {"Character_status": character_stats,
                            "X-coordinate": 0,
                            "Y-coordinate": 0,
                            "EXP": 0,
                            "Items": {"Gold": 0, "Potions": 0},
                            "Equipment": 0,
                            "Buff": 0,
                            "Tutorials": {"Fight": 0, "Talk": 0, "Chest": 0, "Merchant": 0}}
    attribute_points = 10
    add_attribute_points(attribute_points, character_dictionary)
    return character_dictionary


def add_attribute_points(attribute_points, character_dictionary):
    while attribute_points > 0:
        player_point_input = int(input(f"Distribute your attribute points now. You have {attribute_points} points left "
                                       f"to use.\nWhich attribute would you like to increase?\n[1] STR\n[2] DEF\n[3] "
                                       f"CHR\n[4] SPD\n[5] LUK\n"))
        if player_point_input == 1:
            character_dictionary["Character_status"]["STR"] += 1
        elif player_point_input == 2:
            character_dictionary["Character_status"]["DEF"] += 1
        elif player_point_input == 3:
            character_dictionary["Character_status"]["CHR"] += 1
        elif player_point_input == 4:
            character_dictionary["Character_status"]["SPD"] += 1
        else:
            character_dictionary["Character_status"]["LUK"] += 1
        attribute_points -= 1
    print(f"Your stats are: {character_dictionary['Character_status']}\n")



