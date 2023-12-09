"""Text lines for the game go here."""


def get_story(character_dictionary: dict) -> dict:
    main_story = {
        'intro': 'In the small town of Moland there is a ruined dungeon where a dragon sleeps.\n'
                 'It has been prophesized that he will wake up in 100 years to take revenge on the town that sealed '
                 'him.\n'
                 'The 100 years are almost up and the townsfolk are getting restless.\n'
                 'You are a hero that has been hired to take care of the dragon before it\'s too late...\n'
                 'Unfortunately it\'s your first time on the job. This is why you don\'t lie on your resume...\n'
                 'You still have a few days before the prophesized time so you decide to go level up a bit in the '
                 f'nearby field.\n\n{character_dictionary["Name"]}: Guess I\'ll start with these small fry!\n',
        'level 2': f'\n{character_dictionary["Name"]}: Hmm, now I feel a bit stronger '
                   'I think it\'s time to visit the dragon\'s lair.\n'
                   f'{character_dictionary["Name"]}: The townsfolk told me '
                   'it was in a dungeon just past this field.\n'
                   f'{character_dictionary["Name"]}: I hope there isn\'t anything too scary inside...',
        'level 3': 'A loud resounding roar can be heard from deep in the depths of the dungeon.\n '
                   f'{character_dictionary["Name"]}: Uh-oh...did the dragon wake up while I was leveling up?\n'
                   f'You hurry towards the sound.\n',
        'death': f'\n{character_dictionary["Name"]}: ARGHhhHHHHhhHhAAAAHhh...\n'
                 'You died...The town of Moland, helpless against the dragon\'s resurrection, has gone up in flames, '
                 'not a single human spared by the dragon\'s wrath.',
        'win': 'You actually did it! You saved the town of Moland from their unfortunate fate. There will be a great '
               'banquet tonight to celebrate your heroic actions. During the banquet, amongst the drunk townsfolk, '
               'you slowly slip away in the night, ready for your next adventure.',
        'win_talk': 'What a feat! You talked the dragon out of harming the townsfolk! They agreed to swear upon a peace'
                    'treaty and the town of Moland became peaceful once again. There will be a great '
                    'banquet tonight to celebrate your heroic actions. During the banquet, amongst the drunk townsfolk,'
                    ' you slowly slip away in the night, ready for your next adventure.'
    }
    return main_story


welcome = ('Welcome hero!\nIn this game you play as a beginner hero who sets off to make a big name for themself.\n'
           'Your final goal is to reach level 3 and defeat the dragon!\n'
           'For more detailed information about the world and enemies of this game, please read the '
           'game guide section of the README.md\n')

help_lines = {
    "character stats": "First we will begin by slotting your attribute points.\nIn this game there are 7 "
                       "attributes:\n"
                       "[1] HP (Health points) - If HP reaches 0, you die and the game is over.\n"
                       "[2] STR (Strength) - Deal more damage to the enemy.\n"
                       "[3] DEF (Defense) - Defense against enemy damage.\n"
                       "[4] CHR (Charisma) - Avoid battles by talking to monsters.\n"
                       "[5] SPD (Speed) - Allows you to act more often in battle.\n"
                       "[6] LUK (Luck) - Affects lucky map spawn chance and battle escape chance.\n"
                       "[7] VIS (Vision) - How far into the distance you can see.\n"
}

title = f"\n================================================\n"
title += f"              Patricia   Quest\n"
title += f"================================================\n"
