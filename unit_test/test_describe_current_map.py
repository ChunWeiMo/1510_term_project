from modules.exploration.map import maps
from modules.exploration.map import describe_current_map
from unittest import TestCase
from unittest.mock import patch
import io


class TestDescribeCurrentMap(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_level1_map(self, mock_output):
        map_list = maps()
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 0, "Y-coordinate": 4,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        describe_current_map(character_dictionary, map_list[2])
        expected_message = ("There is a big hill and a tall tree in the distance.\nPerhaps there is some treasure"
                            " under it's roots?\n")
        self.assertEqual(expected_message, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_level2_map(self, mock_output):
        map_list = maps()
        character_dictionary = {"Character_status": {"Level": 2, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 0, "Y-coordinate": 4,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        describe_current_map(character_dictionary, map_list[2])
        expected_message = ("The room you enter smells damp and moldy.\n"
                            "It's dark and hard to see where you are going.\n")
        self.assertEqual(expected_message, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_map(self, mock_output):
        map_list = maps()
        character_dictionary = {"Character_status": {"Level": 3, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 0, "Y-coordinate": 4,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        describe_current_map(character_dictionary, map_list[11])
        expected_message = ("You finally enter the boss' chambers.\nIn the middle you see a huge dragon, yawning and"
                            " blinking as if it just woke up.\nThe doors shut behind you with a loud bang, notifying"
                            " the creature of your arrival.\n")
        self.assertEqual(expected_message, mock_output.getvalue())
