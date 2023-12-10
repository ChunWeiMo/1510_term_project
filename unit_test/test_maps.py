from modules.exploration.map import maps
from unittest import TestCase


class TestMaps(TestCase):
    def test_return_maps(self):
        expected_maps = {1: {'Description 1': 'You enter a grassy meadow.\nThere is a merchant getting attacked by a '
                                              'group of monsters!\nWill you help him?\n',
                             'Description 2': 'You enter an old dungeon.\nYou hear skeletons creaking in the '
                                              'distance...surrounding a merchant!\nAgain? What is this guy doing...\n',
                             'Door': [(8, 0), (0, 4), (6, 9)], 'Chest': [(1, 1), (7, 5)],
                             'Enemy': [(6, 1), (2, 3), (3, 4), (1, 5), (2, 5), (4, 5), (6, 5), (3, 6), (4, 6), (7, 6),
                                       (2, 7), (2, 9)],
                             'Merchant': [(3, 5)]},
                         2: {'Description 1': "There is a big hill and a tall tree in the distance.\nPerhaps there is "
                                              "some treasure under it's roots?",
                             'Description 2': "The room you enter smells damp and moldy.\nIt's dark and hard to see "
                                              "where you are going.",
                             'Door': [(5, 0), (4, 9)], 'Chest': [(0, 0), (0, 3), (8, 5)],
                             'Enemy': [(2, 2), (0, 8), (2, 6), (5, 7), (7, 2), (8, 6), (9, 9)],
                             'Merchant': [(4, 4)]},
                         3: {'Description 1': "You wander into a dark forest.\nWhat is wrong with this place! It's "
                                              "swarming with enemies!",
                             'Description 2': "You enter the room and immediately feel the heat increase.\n"
                                              "What's going on in here? The walls are crusted in what looks like "
                                              "cooled lava...",
                             'Door': [(8, 0), (7, 9)], 'Chest': [(5, 2), (2, 7)],
                             'Healing_fountain': [(8, 5)], 'Cerberus': [(5, 6)],
                             'Enemy': [(0, 1), (2, 1), (3, 4), (1, 9), (3, 9), (6, 3), (9, 3), (9, 5)]},
                         4: {'Description 1': 'You find a clearing surrounded by shining lights.\nIt looks like some '
                                              'monsters are having a party here.',
                             'Description 2': 'You shudder at what you see when you walk through the door.\n'
                                              'There is a dark ritual going on this this room, the monsters keep '
                                              'circling and dancing around some treasure.',
                             'Door': [(0, 3), (9, 6)], 'Chest': [(4, 4), (4, 5), (5, 4), (5, 5)],
                             'Enemy': [(1, 0), (2, 0), (3, 1), (4, 1), (9, 1), (5, 2), (9, 2), (4, 3), (5, 3), (2, 4),
                                       (3, 4), (6, 4), (8, 4), (1, 5), (3, 5), (6, 5), (7, 5), (1, 6), (4, 6), (5, 6),
                                       (0, 7), (4, 7), (0, 8), (5, 8), (6, 8), (7, 9), (8, 9)]},
                         5: {'Description 1': "The grassland ends abruptly and an old battlefield lies in front of "
                                              "you.\nThere's some treasure to be found here...",
                             'Description 2': 'You were just in a dark hallway but suddenly this room becomes light '
                                              'and airy as if you just walked into a field of flowers.\n'
                                              'What kind of illusion is this??!',
                             'Door': [(3, 0), (9, 7)], 'Chest': [(6, 2), (1, 4), (4, 7)],
                             'Healing_fountain': [(7, 9)], 'Oberon': [(5, 4)],
                             'Enemy': [(1, 2), (0, 7), (2, 7), (4, 4), (4, 9), (8, 1), (7, 7)]},
                         6: {'Description 1': 'A group of monsters seems to be surrounding something. Do you want to '
                                              'go and investigate?\n',
                             'Description 2': "A group of monsters fiercely guards treasure chests. It's time for a "
                                              "high-risk, high-reward endeavor.\n",
                             'Door': [(4, 0), (9, 4), (0, 5), (5, 9)], 'Chest': [(4, 4), (5, 4), (4, 5), (5, 5)],
                             'Enemy': [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2),
                                       (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (7, 3), (8, 3),
                                       (1, 4), (2, 4), (7, 4), (8, 4), (1, 5), (2, 5), (7, 5), (8, 5), (1, 6), (2, 6),
                                       (7, 6), (8, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7),
                                       (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)],
                             'Dracula': [(5, 3), (4, 6)], 'Merchant': [(3, 5)], 'Healing_fountain': [(3, 4), (6, 4),
                                                                                                     (3, 5), (6, 5)]},
                         7: {'Description 1': "You accidentally stumbled into the monsters' lair. But fortunately, "
                                              "the number of monsters is not large enough to necessitate a fight for "
                                              "your exit.",
                             'Description 2': 'The monsters have formed a maze-like formation, but you can see a safe '
                                              'path leading to the other side.',
                             'Door': [(9, 0), (0, 9)], 'Chest': [(9, 3), (9, 9)],
                             'Enemy': [(3, 0), (3, 1), (7, 1), (7, 2), (8, 2), (9, 2), (1, 3), (2, 3), (3, 3), (4, 3),
                                       (5, 3), (5, 4), (7, 4), (8, 4), (9, 4), (5, 5), (0, 6), (1, 6), (3, 6), (6, 6),
                                       (3, 7), (7, 7), (3, 8), (6, 8), (3, 9)], 'Healing_fountain': [(0, 0), (4, 4)]},
                         8: {'Description 1': "Rumor has it there's a group of monsters known as the 'Newbie Slayers.' "
                                              "Never expected to encounter them here.",
                             'Description 2': "'Hello, adventurer! Impressive that you've made it this far. Now, let "
                                              "our Four Guardians become your opponents!!'",
                             'Door': [(5, 0), (5, 9)], 'Enemy': [(4, 4), (5, 5), (4, 6), (5, 7)],
                             'Chest': [(0, 2), (0, 3)], 'Merchant': [(0, 1)]},
                         9: {'Description 1': 'Who has been digging so many holes in the wilderness?',
                             'Description 2': 'The Chronomancer has altered the structure of this dungeon. '
                                              'Conventional knowledge of entrances and exits no longer seems '
                                              'applicable.',
                             'Door': [(6, 2), (4, 4), (4, 5), (7, 6), (2, 7)], 'Chest': [(0, 0), (9, 9)],
                             'Enemy': [(3, 0), (6, 0), (9, 0), (0, 2), (3, 3), (9, 4), (0, 5), (5, 6), (0, 9), (0, 3),
                                       (0, 7)], 'Healing_fountain': [(6, 4), (3, 6)]},
                         10: {'Description 1': "You discover an abandoned adventurers' guild, and for some reason, "
                                               "the equipment inside has not been taken.\n",
                              'Description 2': 'You unexpectedly entered a treasure vault, with a dazzling array of '
                                               'treasures waiting for you.\n',
                              'Door': [(3, 9), (6, 9)], 'Chest': [(2, 2), (5, 2), (8, 2), (1, 6), (4, 6), (7, 6)],
                              'Merchant': [(0, 0)], 'Healing_fountain': [(4, 4), (6, 4)]},
                         11: {'Description': '', 'Door': [(4, 9), (5, 9)],
                              'Final Boss': [(4, 4), (5, 4), (4, 5), (5, 5)], 'Merchant': [(9, 9)]}}

        self.assertEqual(expected_maps, maps())
