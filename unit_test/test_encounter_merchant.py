import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.exploration.event import encounter_merchant


class TestEncounterMerchant(TestCase):
    def setUp(self):
        self.character_dictionary = {
            "Character_status": {"Level": 2, "HP": 110, "STR": 30, "DEF": 10, "CHR": 1, "SPD": 1,
                                 "LUK": 1, "VIS": 3},
            "Name": "heal", "X-coordinate": 2, "Y-coordinate": 3}
        self.current_map = {(column, row): 'Empty' for row in range(10) for column in range(10)}
        self.current_map[(2, 3)] = "Merchant"

    def test_encounter_merchant(self):
        with unittest.mock.patch('modules.character.items.merchant') as mock_merchant:
            encounter_merchant(self.character_dictionary, self.current_map)
            mock_merchant.assert_called_with(self.character_dictionary)
