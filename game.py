import random
import json
from modules.exploration import map
from modules.exploration import vision
from modules.exploration import movement
from modules.exploration import story_lines
from modules.menu import saveload
from modules.character import character


def main():
    """
    Drive the game.
    """
    achieved_goal = False
    achieved_goal_talk = False
    map_list = map.maps()
    print(story_lines.welcome)
    character_dictionary = character.make_character()
    main_story = story_lines.get_story(character_dictionary)
    print(main_story["intro"])
    command = "not assign"
    current_map = map.create_map(character_dictionary, map_list)
    movement.start_from_door(character_dictionary, current_map)
    while character_dictionary["Character_status"]["HP"] > 0 and not achieved_goal and command.upper != "Q":
        # command = "not assign"
        print()
        vision.print_vision(character_dictionary, current_map)
        movement.describe_current_location(character_dictionary, current_map)
        print("Command list:")
        print("Move a direction: N / E / S / W")
        print("Save or Load a play data: SAVE / LOAD")
        print("Show character stats: STATS")
        print("Quit game: Q")
        command = input("Enter a command: ")
        if command.upper() == 'N' or command.upper() == 'E' or command.upper() == 'S' or command.upper() == 'W':
            direction = command.upper()
            can_move = movement.validate_move(character_dictionary, direction, current_map)
            if can_move:
                movement.move_character(character_dictionary, direction)
                current_map = movement.check_for_event(character_dictionary, current_map)
        elif command.upper() == "STATS":
            print(f'\n{character_dictionary["Character_status"]}')
            print()
        elif command.upper() == 'Q':
            break
        elif command.upper() == 'SAVE':
            saveload.savedata(character_dictionary, current_map)
        elif command.upper() == "LOAD":
            character_dictionary, current_map = saveload.loaddata(character_dictionary, current_map)
        else:
            print("\nInvalid command.")
            print("Please enter a command again.")
    if character_dictionary["Character_status"]["HP"] <= 0:
        print(main_story["death"])
    if achieved_goal:
        print(main_story["win"])
    if achieved_goal_talk:
        print(main_story["win_talk"])
    print("\nThank you for playing.")
    print("Close the game.")


if __name__ == "__main__":
    main()
