from unittest import TestCase
from unittest.mock import patch
from modules.character.character import add_attribute_points
import io


class TestAddPoints(TestCase):
    @patch('builtins.input', side_effect=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_attribute_points_STR(self, mock_output, _):
        attribute_points = 10
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3},
                                "Name": "Chris",
                                "X-coordinate": 0,
                                "Y-coordinate": 0,
                                "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0,
                                "Debuff": {"Burn": 0}
                                }
        add_attribute_points(attribute_points, character_dictionary)
        expected = ("Your stats are: {'Level': 1, 'HP': 100, 'STR': 11, 'DEF': 1, 'CHR': 1, 'SPD': 1, "
                    "'LUK': 1, 'VIS': 3}\n\n")
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('builtins.input', side_effect=[1, 2, 3, 4, 5])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_attribute_points_different(self, mock_output, _):
        attribute_points = 5
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 3,
                                                     "DEF": 2, "CHR": 3, "SPD": 3, "LUK": 1, "VIS": 3},
                                "Name": "Chris",
                                "X-coordinate": 0,
                                "Y-coordinate": 0,
                                "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0,
                                "Debuff": {"Burn": 0}
                                }
        add_attribute_points(attribute_points, character_dictionary)
        expected = ("Your stats are: {'Level': 1, 'HP': 100, 'STR': 4, 'DEF': 3, 'CHR': 4, 'SPD': 4, "
                    "'LUK': 2, 'VIS': 3}\n\n")
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('builtins.input', side_effect=["a", 1, 2, 3, 10, 4, 5])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_incorrect_inputs(self, mock_output, _):
        attribute_points = 5
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 3,
                                                     "DEF": 2, "CHR": 3, "SPD": 3, "LUK": 1, "VIS": 3},
                                "Name": "Chris",
                                "X-coordinate": 0,
                                "Y-coordinate": 0,
                                "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0,
                                "Debuff": {"Burn": 0}
                                }
        add_attribute_points(attribute_points, character_dictionary)
        expected = ("\nPlease enter a number from 1-5.\n\nPlease enter a number from 1-5.\n\n"
                    "Your stats are: {'Level': 1, 'HP': 100, 'STR': 4, 'DEF': 3, 'CHR': 4, 'SPD': 4, "
                    "'LUK': 2, 'VIS': 3}\n\n")
        self.assertEqual(mock_output.getvalue(), expected)
