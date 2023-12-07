from unittest import TestCase
from unittest.mock import patch

from modules.battle.enemy import select_enemy


class TestSelectEnemy(TestCase):
    def setUp(self):
        self.enemy_dictionary = \
            {'Level 1': {1: {'Name': 'Slime', 'HP': 10, 'STR': 2, 'DEF': 1, 'SPD': 2, 'EXP': 3, 'Gold': 1},
                         2: {'Name': 'Pixie', 'HP': 6, 'STR': 2, 'DEF': 1, 'SPD': 3, 'EXP': 3, 'Gold': 1},
                         3: {'Name': 'Wolf', 'HP': 15, 'STR': 3, 'DEF': 1, 'SPD': 2, 'EXP': 5, 'Gold': 1},
                         4: {'Name': 'Skeleton', 'HP': 15, 'STR': 2, 'DEF': 2, 'SPD': 2, 'EXP': 3, 'Gold': 1},
                         5: {'Name': 'Ghost', 'HP': 10, 'STR': 2, 'DEF': 0, 'SPD': 4, 'EXP': 5, 'Gold': 1},
                         6: {'Name': 'Golem', 'HP': 20, 'STR': 1, 'DEF': 5, 'SPD': 0, 'EXP': 5, 'Gold': 1}},
             'Level 2': {1: {'Name': 'Cave Spider', 'HP': 25, 'STR': 1, 'DEF': 2, 'SPD': 5, 'EXP': 3, 'Gold': 2},
                         2: {'Name': 'Skeleton Archer', 'HP': 20, 'STR': 4, 'DEF': 0, 'SPD': 4, 'EXP': 3, 'Gold': 2},
                         3: {'Name': 'Restless Spirit', 'HP': 30, 'STR': 4, 'DEF': 1, 'SPD': 3, 'EXP': 5, 'Gold': 2},
                         4: {'Name': 'Succubus', 'HP': 20, 'STR': 3, 'DEF': 1, 'SPD': 4, 'EXP': 5, 'Gold': 2},
                         5: {'Name': 'Dungeon Maid', 'HP': 25, 'STR': 3, 'DEF': 3, 'SPD': 2, 'EXP': 3, 'Gold': 2},
                         6: {'Name': 'Gargoyle', 'HP': 40, 'STR': 2, 'DEF': 6, 'SPD': 0, 'EXP': 5, 'Gold': 2}},
             'Miniboss': {1: {'Name': 'Cerberus', 'HP': 50, 'STR': 5, 'DEF': 5, 'SPD': 0, 'EXP': 8, 'Gold': 5},
                          2: {'Name': 'Oberon', 'HP': 40, 'STR': 4, 'DEF': 0, 'SPD': 6, 'EXP': 8, 'Gold': 5},
                          3: {'Name': 'Dracula', 'HP': 40, 'STR': 5, 'DEF': 1, 'SPD': 4, 'EXP': 8, 'Gold': 5}},
             'Final Boss': {'Name': 'Evil Dragon', 'HP': 100, 'STR': 7, 'DEF': 4, 'SPD': 3}}

    @patch('modules.battle.enemy.random.randint', return_value=1)
    def test_random_level_1_enemy(self, _):
        character_dictionary = {"Character_status": {"Level": 1}}
        result = select_enemy(character_dictionary, self.enemy_dictionary)
        expected = {'Name': 'Slime', 'HP': 10, 'STR': 2, 'DEF': 1, 'SPD': 2, 'EXP': 3, 'Gold': 1}
        self.assertEqual(result, expected)

    @patch('modules.battle.enemy.random.randint', return_value=3)
    def test_random_level_2_enemy(self, _):
        character_dictionary = {"Character_status": {"Level": 2}}
        result = select_enemy(character_dictionary, self.enemy_dictionary)
        expected = {'Name': 'Restless Spirit', 'HP': 30, 'STR': 4, 'DEF': 1, 'SPD': 3, 'EXP': 5, 'Gold': 2}
        self.assertEqual(result, expected)
