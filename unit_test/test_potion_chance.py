from unittest import TestCase
from unittest.mock import patch
from modules.battle.battle import potion_chance


class TestPotionChance(TestCase):
    @patch('modules.battle.enemy.random.randint', return_value=7)
    def test_roll_7_get_potion(self, _):
        enemy_appeared = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
        character_dictionary = {"EXP": 0, "Items": {"Gold": 0, "Potions": 0}}
        potion_chance(character_dictionary, enemy_appeared)
        expected_char_dict = {"EXP": 0, "Items": {"Gold": 0, "Potions": 1}}
        self.assertEqual(expected_char_dict, character_dictionary)

    @patch('modules.battle.enemy.random.randint', return_value=1)
    def test_roll_1_dont_get_potion(self, _):
        enemy_appeared = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
        character_dictionary = {"EXP": 0, "Items": {"Gold": 0, "Potions": 0}}
        potion_chance(character_dictionary, enemy_appeared)
        expected_char_dict = {"EXP": 0, "Items": {"Gold": 0, "Potions": 0}}
        self.assertEqual(expected_char_dict, character_dictionary)
