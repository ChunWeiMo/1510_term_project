import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.exploration.event import encounter_cerberus
from modules.battle.enemy import enemy


class TestEncounterCerberus(TestCase):
    def setUp(self):
        self.character_dictionary = {
            "Character_status": {"Level": 2, "HP": 110, "STR": 30, "DEF": 1, "CHR": 1, "SPD": 1,
                                 "LUK": 1, "VIS": 3},
            "Name": "describe", "X-coordinate": 7, "Y-coordinate": 1,
            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
            "Equipment": 0, "Debuff": {"Burn": 0}}

        self.enemy_dictionary = enemy()
        self.current_map = {(column, row): 'Empty' for row in range(10) for column in range(10)}
        self.current_map[(7, 1)] = "Cerberus"

    def test_encounter_Cerberus(self):
        with unittest.mock.patch('modules.battle.enemy.ask_user') as mock_ask_user:
            encounter_cerberus(self.character_dictionary, self.current_map)
            enemy_appeared = self.enemy_dictionary["Miniboss"][1]
            mock_ask_user(enemy_appeared)
