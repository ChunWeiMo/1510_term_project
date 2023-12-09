import io
from unittest import TestCase
from unittest.mock import patch
from modules.battle.battle import level_up


class TestLevelUp(TestCase):
    @patch('builtins.input', side_effect=[1, 2, 3, 4, 5])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_level_up_to_level_2(self, mock_output, _):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}, "Name": "nori"}
        level_up(character_dictionary)
        expected = ("You leveled up! You are now level 2.\n\n"
                    "\nnori: Hmm, now I feel a bit stronger I think it's time to visit the dragon's lair.\n"
                    "nori: The townsfolk told me it was in a dungeon just past this field.\n"
                    "nori: I hope there isn't anything too scary inside...\n"
                    "Your stats are: {'Level': 2, 'HP': 120, 'STR': 2, 'DEF': 6, "
                    "'CHR': 2, 'SPD': 2, 'LUK': 2, 'VIS': 3}\n\n")
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=[1, 1, 1, 1, 1])
    def test_level_up_to_level_2(self, _):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "Name": "nori"}
        level_up(character_dictionary)
        expected = {"Character_status": {"Level": 2, "HP": 120, "STR": 6,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                    "Name": "nori"}
        self.assertEqual(expected, character_dictionary)

    @patch('builtins.input', side_effect=[1, 1, 1, 1, 1])
    def test_level_up_to_level_3(self, _):
        character_dictionary = {"Character_status": {"Level": 2, "HP": 120, "STR": 6,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Name": "nori"}
        level_up(character_dictionary)
        expected = {"Character_status": {"Level": 3, "HP": 150, "STR": 11,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                    "Name": "nori"}
        self.assertEqual(expected, character_dictionary)
