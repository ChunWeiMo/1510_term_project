import io
from unittest import TestCase
from unittest.mock import patch

from modules.battle.battle import boss_fireball


class TestFireball(TestCase):
    def test_character_def_less_than_boss_str(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1, "DEF": 1,
                                                          "CHR": 1, "SPD": 1, "LUK": 1}, "Debuff": {"Burn": 0}}
        enemy_appeared = {"Name": "Evil Dragon", "HP": 100, "STR": 7, "DEF": 4, "SPD": 3, "EXP": 10, "Gold": 10}
        boss_fireball(character_dictionary, enemy_appeared)
        expected = {"Character_status": {"Level": 1, "HP": 92, "STR": 1, "DEF": 1,
                                                          "CHR": 1, "SPD": 1, "LUK": 1}, "Debuff": {"Burn": 3}}
        self.assertEqual(expected, character_dictionary)

    def test_character_def_more_than_boss_str(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1, "DEF": 10,
                                                          "CHR": 1, "SPD": 1, "LUK": 1}, "Debuff": {"Burn": 0}}
        enemy_appeared = {"Name": "Evil Dragon", "HP": 100, "STR": 7, "DEF": 4, "SPD": 3, "EXP": 10, "Gold": 10}
        boss_fireball(character_dictionary, enemy_appeared)
        expected = {"Character_status": {"Level": 1, "HP": 97, "STR": 1, "DEF": 10,
                                                          "CHR": 1, "SPD": 1, "LUK": 1}, "Debuff": {"Burn": 3}}
        self.assertEqual(expected, character_dictionary)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_hp_is_zero(self, mock_output):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 0, "STR": 1, "DEF": 10,
                                                          "CHR": 1, "SPD": 1, "LUK": 1}, "Debuff": {"Burn": 0}}
        enemy_appeared = {"Name": "Evil Dragon", "HP": 100, "STR": 7, "DEF": 4, "SPD": 3, "EXP": 10, "Gold": 10}
        boss_fireball(character_dictionary, enemy_appeared)
        expected = ("\nThe dragon takes a deep breath, his throat glowing bright orange.\n"
                    "Next thing you know the room is filled with flames.\n\n"
                    "The Evil Dragon dealt 3 damage to you!\nYou have 0 HP left.\n\n")
        self.assertEqual(expected, mock_output.getvalue())
