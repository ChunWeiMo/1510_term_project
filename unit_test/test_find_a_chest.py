import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.exploration.event import find_a_chest


class TestFindAChest(TestCase):
    def setUp(self):
        self.character_dictionary = {
            "Character_status": {"Level": 2, "HP": 110, "STR": 30, "DEF": 10, "CHR": 1, "SPD": 1,
                                 "LUK": 1, "VIS": 3},
            "Name": "describe", "X-coordinate": 2, "Y-coordinate": 6,
            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
            "Equipment": 0, "Debuff": {"Burn": 0}}

        self.current_map = {(column, row): 'Empty' for row in range(10) for column in range(10)}
        self.current_map[(2, 6)] = "Chest"

    def test_find_a_chest(self):
        with unittest.mock.patch('modules.character.equipment.get_equipment') as mock_get_equipment:
            find_a_chest(self.character_dictionary, self.current_map)
            mock_get_equipment.assert_called_with(self.character_dictionary)
