import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.battle.battle import boss_battle


class TestBossBattle(TestCase):

    @patch('builtins.input', side_effect=[1])
    def test_boss_hp_reaches_zero(self, _):
        character_dictionary = {
            "Character_status": {"HP": 100}, "Debuff": {"Burn": 0}}
        enemy_appeared = {"HP": 0}
        turn = "character"
        result = boss_battle(character_dictionary, enemy_appeared, turn)
        expected = None
        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=[1])
    def test_player_hp_reach_zero(self, _):
        character_dictionary = {"Character_status": {"HP": 0}, "Debuff": {"Burn": 0}}
        enemy_appeared = {"HP": 100}
        turn = "character"
        result = boss_battle(character_dictionary, enemy_appeared, turn)
        expected = None
        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=[1])
    def test_boss_battle_player_burnt_to_death(self, _):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 5, "STR": 1, "DEF": 5,
                                                     "CHR": 1, "SPD": 1, "LUK": 1}, "Debuff": {"Burn": 3}}
        enemy_appeared = {"Name": "Evil Dragon", "HP": 100, "STR": 7, "DEF": 4, "SPD": 3, "EXP": 10, "Gold": 10}
        turn = "character"
        result = boss_battle(character_dictionary, enemy_appeared, turn)
        self.assertFalse(result)

    @patch('modules.battle.enemy.random.randint', return_value=3)
    @patch('builtins.input', side_effect=[1,1,1,1,1])
    def test_boss_battle_player_burnt_once(self, _, __):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 20, "STR": 1000, "DEF": 5, "CHR": 1,
                                                     "SPD": 1, "LUK": 1}, "Debuff": {"Burn": 3}}
        enemy_appeared = {"Name": "Evil Dragon", "HP": 100, "STR": 7, "DEF": 4, "SPD": 3, "EXP": 10, "Gold": 10}
        turn = "character"
        boss_battle(character_dictionary, enemy_appeared, turn)
        expected = {"Character_status": {"Level": 1, "HP": 15, "STR": 1000, "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1},
                     "Debuff": {"Burn": 3}}
        self.assertEqual(character_dictionary, expected)
