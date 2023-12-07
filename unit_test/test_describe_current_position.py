from modules.exploration.movement import describe_current_location
from unittest import TestCase
from unittest.mock import patch
import io


class TestDescribeCurrentLocation(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_in_map(self, mock_output):
        character_dictionary = {"Character_status": {"Level": 2, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 7, "Y-coordinate": 5,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(column, row): "Empty" for row in range(10) for column in range(10)}
        expected_message = "You are at X: 7, Y: 5.\n\n"
        describe_current_location(character_dictionary, current_map)
        self.assertEqual(expected_message, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_out_map(self, mock_output):
        character_dictionary = {"Character_status": {"Level": 2, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 11, "Y-coordinate": 5,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(column, row): "Empty" for row in range(10) for column in range(10)}
        expected_message = "You are at X: 11, Y: 5.\n\n!!WARNING!!: Out of the board\n\n"
        describe_current_location(character_dictionary, current_map)
        self.assertEqual(expected_message, mock_output.getvalue())
