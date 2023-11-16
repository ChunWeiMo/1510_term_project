"""
Character module.
"""


import time


def make_character():
    character = {"Level": 1, "HP": 100, "STR": 1, "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1}
    print("Welcome Hero! In this game there are 6 attributes:\n"
          "[1] HP (Health points) - When this reaches 0, you die and the game is over.\n"
          "[2] STR (Strength) - Deal more damage to the enemy.\n"
          "[3] DEF (Defense) - Defense against enemy damage.\n"
          "[4] CHR (Charisma) - Avoid battles by talking to monsters.\n"
          "[5] SPD (Speed) - Allows you to act more often in battle\n"
          "[6] LUK (Luck) - Affects lucky map spawn chance\n")
    time.sleep(3)
    attribute_points = 10
    add_attribute_points(attribute_points, character)
    return character


def add_attribute_points(attribute_points, character):
    while attribute_points > 0:
        player_point_input = int(input(f"Distribute your attribute points now. You have {attribute_points} points left "
                                       f"to use.\nWhich attribute would you like to increase?\n[1] STR\n[2] DEF\n[3] "
                                       f"CHR\n[4] SPD\n[5] LUK\n"))
        if player_point_input == 1:
            character["STR"] += 1
        elif player_point_input == 2:
            character["DEF"] += 1
        elif player_point_input == 3:
            character["CHR"] += 1
        elif player_point_input == 4:
            character["SPD"] += 1
        else:
            character["LUK"] += 1
        attribute_points -= 1
    print(f"Your stats are: {character}\n")

