from unittest import TestCase
from modules.exploration.event import rest_at_fountain


class TestRestAtFountain(TestCase):
    def setUp(self):
        self.character_dictionary = {
            "Character_status": {"Level": 2, "HP": 110, "STR": 30, "DEF": 10, "CHR": 1, "SPD": 1,
                                 "LUK": 1, "VIS": 3},
            "Name": "heal", "X-coordinate": 1, "Y-coordinate": 7}
        self.current_map = {(column, row): 'Empty' for row in range(10) for column in range(10)}
        self.current_map[(1, 7)] = "Healing_fountain"

    def test_rest_at_fountain(self):
        rest_at_fountain(self.character_dictionary, self.current_map)
        expected_character_dictionary = {
            "Character_status": {"Level": 2, "HP": 115, "STR": 30, "DEF": 10, "CHR": 1, "SPD": 1,
                                 "LUK": 1, "VIS": 3},
            "Name": "heal", "X-coordinate": 1, "Y-coordinate": 7}
        self.assertEqual(expected_character_dictionary, self.character_dictionary)
