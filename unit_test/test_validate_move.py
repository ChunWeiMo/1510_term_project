from modules.exploration.movement import validate_move
from unittest import TestCase
from unittest.mock import patch
import io


class TestValidateMove(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_stop_by_north_wall(self, mock_output):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 0, "Y-coordinate": 0,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(0, 0): 'Empty', (1, 0): 'Empty', (0, 1): 'Empty', (1, 1): 'Empty'}
        validate_move(character_dictionary, "N", current_map)
        expected_message = 'You are stopped by North wall\n\n'
        expected_can_move = False
        self.assertEqual(expected_message, mock_output.getvalue())
        self.assertEqual(expected_can_move, validate_move(character_dictionary, "N", current_map))

    def test_move_east(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 12, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 0, "Y-coordinate": 0,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(0, 0): 'Empty', (1, 0): 'Empty', (0, 1): 'Empty', (1, 1): 'Door'}
        expected_can_move = True
        self.assertEqual(expected_can_move, validate_move(character_dictionary, "E", current_map))

    def test_move_south(self):
        character_dictionary = {"Character_status": {"Level": 2, "HP": 100, "STR": 12, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 0, "Y-coordinate": 0,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(0, 0): 'Door', (1, 0): 'Empty', (0, 1): 'Empty', (1, 1): 'Empty'}
        expected_can_move = True
        self.assertEqual(expected_can_move, validate_move(character_dictionary, "S", current_map))
