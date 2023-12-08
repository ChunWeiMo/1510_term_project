import unittest
import io
from unittest import TestCase
from unittest.mock import patch
from modules.exploration.event import open_the_door
from modules.exploration.map import maps
from modules.exploration.map import create_map


class TestOpenTheDoor(TestCase):
    def setUp(self):
        self.character_dictionary = {
            "Character_status": {"Level": 2, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                 "LUK": 1, "VIS": 3},
            "Name": "describe", "X-coordinate": 7, "Y-coordinate": 1,
            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
            "Equipment": 0, "Debuff": {"Burn": 0}}

        self.map_list = maps()
        self.current_map = {(column, row): 'Empty' for row in range(10) for column in range(10)}

    @patch('random.randint', side_effect=[2, 2])
    @patch('builtins.input', side_effect=['Y'])
    def test_input_Y_to_open_the_door_to_a_new_random_map(self, _, __):
        with unittest.mock.patch('modules.exploration.movement.start_from_door') as mock_start_from_door:
            open_the_door(self.character_dictionary, self.current_map)
            current_map = create_map(self.character_dictionary, self.map_list)
            mock_start_from_door.assert_called_with(self.character_dictionary, current_map)

    @patch('builtins.input', side_effect=['N'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_N_to_not_open_the_door(self, mock_output, __):
        open_the_door(self.character_dictionary, self.current_map)
        expected_message = "Maybe there is still something to explore here?\n"
        self.assertEqual(expected_message, mock_output.getvalue())

    @patch('builtins.input', side_effect=['A'])
    def test_invalid_input(self, _):
        with self.assertRaises(StopIteration):
            open_the_door(self.character_dictionary, self.current_map)
