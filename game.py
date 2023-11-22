"""
Chun-Wei Mo
A________

Patricia Lo
A00959925
"""
import character
import map
import enemy


def game():
    """
    Drive the game.
    """
    achieved_goal = False
    map_list = map.make_maps()
    character_dictionary = character.make_character()
    print("In the small town of Moland there is a ruined dungeon where a dragon sleeps.\n"
          "It has been prophesized that he will wake up in 100 years to take revenge on the town that sealed him.\n"
          "The 100 years are almost up and the townsfolk are getting restless.\n"
          "You are a hero that has been hired to take care of the dragon before it's too late...\n"
          "Unfortunately it's your first time on the job. This is why you don't lie on your resume...\n"
          "You still have a few days before the prophesized time so you decide to go level up a bit in the "
          "nearby field.\n")
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
            print("A loud resounding roar can be heard from deep in the depths of the dungeon. Uh-oh...did the dragon "
                  "wake up while you were leveling up? You hurry towards the sound.")
            # next map you enter will be boss map
            current_map = map.select_map(character_dictionary, map_list)
    if character_dictionary["Character_status"]["HP"] == 0:
        print("You died...The town of Moland, helpless against the dragon's resurrection, has gone up in flames, "
              "not a single human spared by the dragon's wrath.")
    if achieved_goal:
        print("You actually did it! You saved the town of Moland from their unfortunate fate. There will be a great "
              "banquet tonight to celebrate your heroic actions. During the banquet, amongst the drunk townsfolk, "
              "you slowly slip away in the night, ready for your next adventure.")


def main():
    """
    Run the program.
    """
    game()


if __name__ == "__main__":
    main()
