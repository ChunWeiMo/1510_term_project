"""
Character module.
"""
import time
import map
import random


def make_character():
    character_stats = {"Level": 1, "HP": 100, "STR": 1,
                       "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1}
    print("Welcome Hero! In this game there are 6 attributes:\n"
          "[1] HP (Health points) - If HP reaches 0, you die and the game is over.\n"
          "[2] STR (Strength) - Deal more damage to the enemy.\n"
          "[3] DEF (Defense) - Defense against enemy damage.\n"
          "[4] CHR (Charisma) - Avoid battles by talking to monsters.\n"
          "[5] SPD (Speed) - Allows you to act more often in battle\n"
          "[6] LUK (Luck) - Affects lucky map spawn chance\n")
    time.sleep(3)
    attribute_points = 10
    add_attribute_points(attribute_points, character_stats)
    return {"Character_status": character_stats, "X-coordinate": 0, "Y-coordinate": 0}


def add_attribute_points(attribute_points, character_stats):
    while attribute_points > 0:
        player_point_input = int(input(f"Distribute your attribute points now. You have {attribute_points} points left "
                                       f"to use.\nWhich attribute would you like to increase?\n[1] STR\n[2] DEF\n[3] "
                                       f"CHR\n[4] SPD\n[5] LUK\n"))
        if player_point_input == 1:
            character_stats["STR"] += 1
        elif player_point_input == 2:
            character_stats["DEF"] += 1
        elif player_point_input == 3:
            character_stats["CHR"] += 1
        elif player_point_input == 4:
            character_stats["SPD"] += 1
        else:
            character_stats["LUK"] += 1
        attribute_points -= 1
    print(f"Your stats are: {character_stats}\n")


def start_from_door(map_elements, character):
    doors = map_elements["Door"]
    door_rand = doors[random.randint(0, len(doors)-1)]
    character["X-coordinate"] = door_rand[0]
    character["Y-coordinate"] = door_rand[1]
    

def validate_move(current_map, character, direction):
    north_wall, west_all = 0, 0
    south_wall, east_wall = map.walls(current_map)
    can_move = True
    if character["Y-coordinate"] <= north_wall and direction == 0:
        can_move = False
        print("You are stopped by North wall\n")
    if character["X-coordinate"] >= east_wall and direction == 1:
        can_move = False
        print("You are stopped by East wall\n")
    if character["Y-coordinate"] >= south_wall and direction == 2:
        can_move = False
        print("You are stopped by South wall\n")
    if character["X-coordinate"] <= west_all and direction == 3:
        can_move = False
        print("You are stopped by West wall\n")
    return can_move


def move_character(character, direction):
    if direction == 0:
        character["Y-coordinate"] -= 1
        print("moving toward North...")
    if direction == 1:
        character["X-coordinate"] += 1
        print("moving toward East...")
    if direction == 2:
        character["Y-coordinate"] += 1
        print("moving toward South...")
    if direction == 3:
        character["X-coordinate"] -= 1
        print("moving toward West...")
