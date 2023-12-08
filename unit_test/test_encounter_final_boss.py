import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.exploration.event import encounter_final_boss
from modules.battle.enemy import enemy


class TestEncounterFinalBoss(TestCase):
    def setUp(self):
        self.enemy_dictionary = enemy()
        self.current_map = {(column, row): 'Empty' for row in range(10) for column in range(10)}
        self.current_map[(5, 5)] = "Final Boss"

    @patch('builtins.input', side_effect=[1, 1])
    def test_encounter_Final_Boss_and_win(self, _):
        character_dictionary = {
            "Character_status": {"Level": 3, "HP": 110, "STR": 500, "DEF": 100, "CHR": 1, "SPD": 1,
                                 "LUK": 1, "VIS": 3},
            "Name": "describe", "X-coordinate": 5, "Y-coordinate": 5,
            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
            "Equipment": 0, "Debuff": {"Burn": 0}}
        expected_achieve_goal = True
        self.assertEqual(expected_achieve_goal, encounter_final_boss(character_dictionary, self.current_map))

    @patch('builtins.input', side_effect=[1, 1])
    def test_encounter_Final_Boss_and_loss(self, _):
        character_dictionary = {
            "Character_status": {"Level": 3, "HP": 1, "STR": 1, "DEF": 1, "CHR": 1, "SPD": 1,
                                 "LUK": 1, "VIS": 3},
            "Name": "describe", "X-coordinate": 5, "Y-coordinate": 5,
            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
            "Equipment": 0, "Debuff": {"Burn": 0}}
        expected_achieve_goal = False
        self.assertEqual(expected_achieve_goal, encounter_final_boss(character_dictionary, self.current_map))