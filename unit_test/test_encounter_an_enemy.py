import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.exploration.event import encounter_an_enemy
from modules.battle.enemy import enemy
from modules.battle.enemy import select_enemy
from modules.battle.enemy import ask_user


class TestEncounterAnEnemy(TestCase):
    def setUp(self):
        self.character_dictionary = {
            "Character_status": {"Level": 1, "HP": 100, "STR": 30, "DEF": 1, "CHR": 1, "SPD": 1,
                                 "LUK": 1, "VIS": 3},
            "Name": "describe", "X-coordinate": 7, "Y-coordinate": 1,
            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
            "Equipment": 0, "Debuff": {"Burn": 0}}

        self.enemy_dictionary = enemy()
        self.current_map = {(column, row): 'Empty' for row in range(10) for column in range(10)}
        self.current_map[(7, 1)] = "Enemy"

    @patch('random.randint', side_effect=[1, 1])
    @patch('builtins.input', side_effect=[1, 1])
    def test_encounter_a_level_enemy_1_and_battle(self, _, __):
        with unittest.mock.patch('modules.battle.enemy.battle_talk_escape') as mock_battle_talk_escape:
            encounter_an_enemy(self.character_dictionary, self.current_map)
            enemy_appeared = select_enemy(self.character_dictionary, self.enemy_dictionary)
            user_input = ask_user(enemy_appeared)
            mock_battle_talk_escape.assert_called_with(self.character_dictionary, user_input, enemy_appeared)

    @patch('random.randint', side_effect=[2, 2])
    @patch('builtins.input', side_effect=[2, 2])
    def test_encounter_a_level_1_enemy_and_talk(self, _, __):
        with unittest.mock.patch('modules.battle.enemy.battle_talk_escape') as mock_battle_talk_escape:
            encounter_an_enemy(self.character_dictionary, self.current_map)
            enemy_appeared = select_enemy(self.character_dictionary, self.enemy_dictionary)
            user_input = ask_user(enemy_appeared)
            mock_battle_talk_escape.assert_called_with(self.character_dictionary, user_input, enemy_appeared)

    @patch('random.randint', side_effect=[3, 3])
    @patch('builtins.input', side_effect=[3, 3])
    def test_encounter_a_level_1_enemy_and_use_item(self, _, __):
        with unittest.mock.patch('modules.battle.enemy.battle_talk_escape') as mock_battle_talk_escape:
            encounter_an_enemy(self.character_dictionary, self.current_map)
            enemy_appeared = select_enemy(self.character_dictionary, self.enemy_dictionary)
            user_input = ask_user(enemy_appeared)
            mock_battle_talk_escape.assert_called_with(self.character_dictionary, user_input, enemy_appeared)

    @patch('random.randint', side_effect=[4, 4])
    @patch('builtins.input', side_effect=[4, 4])
    def test_encounter_a_level_1_enemy_and_run_away(self, _, __):
        with unittest.mock.patch('modules.battle.enemy.battle_talk_escape') as mock_battle_talk_escape:
            encounter_an_enemy(self.character_dictionary, self.current_map)
            enemy_appeared = select_enemy(self.character_dictionary, self.enemy_dictionary)
            user_input = ask_user(enemy_appeared)
            mock_battle_talk_escape.assert_called_with(self.character_dictionary, user_input, enemy_appeared)

    @patch('builtins.input', side_effect=[5])
    def test_invalid_input(self, _):
        with self.assertRaises(StopIteration):
            encounter_an_enemy(self.character_dictionary, self.current_map)
