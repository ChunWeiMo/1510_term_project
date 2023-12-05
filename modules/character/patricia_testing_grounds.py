"""
Chun-Wei Mo
A01375071

Patricia Lo
A00959925
"""
from modules.character import character
from modules.exploration import map, movement
from modules.battle import enemy
from modules.battle import battle
from modules.exploration import story_lines


def game():
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
    while character_dictionary["Character_status"]["HP"] > 0 and not achieved_goal:
        enemy_dictionary = enemy.enemy()
        if character_dictionary["Character_status"]["Level"] < 3:
            current_map = map.select_map(character_dictionary, map_list)
            map.describe_current_map(character_dictionary, current_map)
            movement.start_from_door(character_dictionary, current_map)
            # encounters?

            # combat starts when you encounter an enemy
            # enemy_appeared = enemy.select_enemy(character_dictionary, enemy_dictionary)
            enemy_appeared = enemy_dictionary["Miniboss"][3]
            user_input = enemy.ask_user(enemy_appeared)
            enemy.battle_talk_escape(character_dictionary, user_input, enemy_appeared)
        else:
            print(main_story["level 3"])

            # next map you enter will be boss map
            current_map = map_list[11]
            map.describe_current_map(character_dictionary, current_map)

            # when you encounter final boss
            enemy_appeared = enemy_dictionary["Final Boss"]
            user_input = enemy.ask_user(enemy_appeared)
            enemy.battle_talk_escape(character_dictionary, user_input, enemy_appeared)
    if character_dictionary["Character_status"]["HP"] <= 0:
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
