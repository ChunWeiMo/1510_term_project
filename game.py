"""
Chun-Wei Mo
A01375071

Patricia Lo
A00959925
"""
from modules.character import character
from modules.exploration import map
from modules.battle import enemy
from modules.exploration import story_lines


def game():
    """
    Drive the game.
    """
    achieved_goal = False
    achieved_goal_talk = False
    map_list = map.map_list()
    print(story_lines.welcome)
    character_dictionary = character.make_character()
    main_story = story_lines.get_story(character_dictionary)
    print(main_story["intro"])
    while character_dictionary["Character_status"]["HP"] > 0 and not achieved_goal:
        if character_dictionary["Character_status"]["Level"] < 3:
            current_map = map.select_map(character_dictionary, map_list)
            map.describe_current_map(character_dictionary, current_map)
            # move around map

            # encounters?

            # combat starts when you encounter an enemy
            enemy_dictionary = enemy.enemy()
            enemy_appeared = enemy.select_enemy(character_dictionary, enemy_dictionary)
            user_input = enemy.ask_user(enemy_appeared)
            enemy.battle_talk_escape(character_dictionary, user_input, enemy_appeared)
        else:
            print(story_lines.main_story["level 3"])
            # next map you enter will be boss map
            current_map = map.select_map(character_dictionary, map_list)
    if character_dictionary["Character_status"]["HP"] == 0:
        print(main_story["death"])
    if achieved_goal:
        print(main_story["win"])
    if achieved_goal_talk:
        print(main_story["win_talk"])


def main():
    """
    Run the program.
    """
    game()


if __name__ == "__main__":
    main()
