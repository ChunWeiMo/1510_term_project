import io
from unittest import TestCase
from unittest.mock import patch
from modules.battle.battle import is_character_dead


class TestEnemyDead(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_hp_greater_than_zero(self, mock_output):
        enemy_appeared = {"Name": "Slime", "HP": 9, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        damage = 1
        is_character_dead(character_dictionary, enemy_appeared, damage)
        expected = (f"{enemy_appeared['Name']} dealt {damage} damage to you!\n"
                    f"You have {character_dictionary['Character_status']['HP']} HP left.\n\n")
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_hp_less_than_zero(self, mock_output):
        enemy_appeared = {"Name": "Slime", "HP": 20, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
        character_dictionary = {"Character_status": {"Level": 1, "HP": 0, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 10, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        damage = 1
        is_character_dead(character_dictionary, enemy_appeared, damage)
        expected = f"{enemy_appeared['Name']} dealt {damage} damage to you!\nYou have 0 HP left.\n"
        self.assertEqual(mock_output.getvalue(), expected)
