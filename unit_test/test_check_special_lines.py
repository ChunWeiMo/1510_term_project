import io
from unittest import TestCase
from unittest.mock import patch

from modules.battle.talk import check_special_lines


class TestCheckSpecialLines(TestCase):
    def setUp(self) -> None:
        self.response_options = {1: "Sure...(-5 HP)",
                                 2: "Ok, if you leave me alone (-10 Gold)",
                                 3: "Hmmm if it is the only way. (HP -20)"}

    def test_line_that_reduce_hp_by_5(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        response = 1
        check_special_lines(response, self.response_options, character_dictionary)
        expected = {"Character_status": {"Level": 1, "HP": 95, "STR": 1,
                                         "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                    "Items": {"Gold": 0, "Potions": 0}}
        self.assertEqual(expected, character_dictionary)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_line_that_reduce_hp_by_5_but_character_dies(self, mock_output):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 2, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 5, "Potions": 0}}
        response = 1
        check_special_lines(response, self.response_options, character_dictionary)
        expected = "I only have 2 HP left...\nThis is it for me.\n\n"
        self.assertEqual(expected, mock_output.getvalue())

    def test_line_that_reduce_gold_by_10(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 10, "Potions": 0}}
        response = 2
        check_special_lines(response, self.response_options, character_dictionary)
        expected = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                         "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                    "Items": {"Gold": 0, "Potions": 0}}
        self.assertEqual(expected, character_dictionary)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_line_that_reduce_gold_by_10_not_enough_gold(self, mock_output):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 5, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 5, "Potions": 0}}
        response = 2
        check_special_lines(response, self.response_options, character_dictionary)
        expected = "I only have 5 gold left...\nTake it.\n\n"
        self.assertEqual(expected, mock_output.getvalue())

    def test_line_that_reduce_hp_by_20(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        response = 3
        check_special_lines(response, self.response_options, character_dictionary)
        expected = {"Character_status": {"Level": 1, "HP": 80, "STR": 1,
                                         "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                    "Items": {"Gold": 0, "Potions": 0}}
        self.assertEqual(expected, character_dictionary)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_line_that_reduce_hp_by_20_and_char_dies(self, mock_output):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 5, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        response = 3
        check_special_lines(response, self.response_options, character_dictionary)
        expected = "I only have 5 HP left...\nThis is it for me.\n\n"
        self.assertEqual(expected, mock_output.getvalue())
