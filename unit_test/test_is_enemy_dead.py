import io
from unittest import TestCase
from unittest.mock import patch
from modules.battle.battle import is_enemy_dead


class TestEnemyDead(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_enemy_hp_greater_than_zero(self, mock_output):
        enemy_appeared = {"Name": "Slime", "HP": 9, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
        damage = 1
        is_enemy_dead(enemy_appeared, damage)
        expected = (f"\nYou deal {damage} damage to {enemy_appeared['Name']}!\nThe {enemy_appeared['Name']} has "
                    f"{enemy_appeared['HP']} HP left.\n\n")
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_enemy_hp_less_than_zero(self, mock_output):
        enemy_appeared = {"Name": "Slime", "HP": 0, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
        damage = 10
        is_enemy_dead(enemy_appeared, damage)
        expected = (f"\nYou deal {damage} damage to {enemy_appeared['Name']}!\nThe "
                    f"{enemy_appeared['Name']} has 0 HP left.\n\n")
        self.assertEqual(mock_output.getvalue(), expected)
