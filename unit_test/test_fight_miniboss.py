from unittest import TestCase
from unittest.mock import patch
from modules.battle.battle import fight_miniboss


class TestFightMiniboss(TestCase):
    @patch('builtins.input', side_effect=[1])
    def test_enemy_hp_is_zero(self, _):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        enemy_appeared = {"Name": "Slime", "HP": 0, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
        result = fight_miniboss(character_dictionary, enemy_appeared)
        expected = True
        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=[1])
    def test_character_hp_is_zero(self, _):
        character_dictionary = {"Character_status": {"HP": 0}}
        enemy_appeared = {"HP": 20}
        result = fight_miniboss(character_dictionary, enemy_appeared)
        expected = False
        self.assertEqual(result, expected)
