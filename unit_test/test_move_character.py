from modules.exploration.movement import move_character
from unittest import TestCase
from unittest.mock import patch
import io


class TestMoveCharacter(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_move_north(self, mock_output):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 4, "Y-coordinate": 5,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        expected_message = "moving toward North...\n"
        expected_character_dictionary = {
            "Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                 "LUK": 1, "VIS": 3},
            "Name": "describe", "X-coordinate": 4, "Y-coordinate": 4,
            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
            "Equipment": 0, "Debuff": {"Burn": 0}}
        direction = "N"
        move_character(character_dictionary, direction)
        self.assertEqual(expected_message, mock_output.getvalue())
        self.assertEqual(expected_character_dictionary, character_dictionary)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_south(self, mock_output):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 5, "Y-coordinate": 5,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        expected_message = "moving toward South...\n"
        expected_character_dictionary = {
            "Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                 "LUK": 1, "VIS": 3},
            "Name": "describe", "X-coordinate": 5, "Y-coordinate": 6,
            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
            "Equipment": 0, "Debuff": {"Burn": 0}}
        direction = "S"
        move_character(character_dictionary, direction)
        self.assertEqual(expected_message, mock_output.getvalue())
        self.assertEqual(expected_character_dictionary, character_dictionary)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_east(self, mock_output):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 3, "Y-coordinate": 3,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        expected_message = "moving toward East...\n"
        expected_character_dictionary = {
            "Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                 "LUK": 1, "VIS": 3},
            "Name": "describe", "X-coordinate": 4, "Y-coordinate": 3,
            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
            "Equipment": 0, "Debuff": {"Burn": 0}}
        direction = "E"
        move_character(character_dictionary, direction)
        self.assertEqual(expected_message, mock_output.getvalue())
        self.assertEqual(expected_character_dictionary, character_dictionary)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_west(self, mock_output):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 3, "Y-coordinate": 2,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        expected_message = "moving toward West...\n"
        expected_character_dictionary = {
            "Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                 "LUK": 1, "VIS": 3},
            "Name": "describe", "X-coordinate": 2, "Y-coordinate": 2,
            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
            "Equipment": 0, "Debuff": {"Burn": 0}}
        direction = "W"
        move_character(character_dictionary, direction)
        self.assertEqual(expected_message, mock_output.getvalue())
        self.assertEqual(expected_character_dictionary, character_dictionary)