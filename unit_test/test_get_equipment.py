from unittest import TestCase
from unittest.mock import patch
from modules.character.equipment import get_equipment


class TestGetEquipment(TestCase):
    @patch('random.randint', side_effect=[1])
    def test_get_leve1_equipment(self, _):
        character_dictionary = {
            "Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 5, "CHR": 5, "SPD": 5, "LUK": 5, "VIS": 2},
            "Equipment": 0}
        expected_equipment = ["Steel sword", ("STR", 3)]
        self.assertEqual(expected_equipment, get_equipment(character_dictionary))

    @patch('random.randint', side_effect=[2])
    def test_get_leve2_equipment(self, _):
        character_dictionary = {
            "Character_status": {"Level": 2, "HP": 100, "STR": 11, "DEF": 5, "CHR": 5, "SPD": 5, "LUK": 5, "VIS": 2},
            "Equipment": 0}
        expected_equipment = ["Hero's spear", ("STR", 5), ("SPD", 2)]
        self.assertEqual(expected_equipment, get_equipment(character_dictionary))

    @patch('random.randint', side_effect=[4])
    def test_get_leve3_equipment(self, _):
        character_dictionary = {
            "Character_status": {"Level": 3, "HP": 100, "STR": 11, "DEF": 5, "CHR": 5, "SPD": 5, "LUK": 5, "VIS": 2},
            "Equipment": 0}
        expected_equipment = ["Dragon slayer", ("STR", 10), ("STR", 5)]
        self.assertEqual(expected_equipment, get_equipment(character_dictionary))
