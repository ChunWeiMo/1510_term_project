import io
from unittest import TestCase
from unittest.mock import patch
from modules.battle.battle import cure_hp


class TestCureHP(TestCase):
    def test_dracula_hp_plus_cure_heals_to_max(self):
        enemy_appeared = {"Name": "Dracula", "HP": 37, "STR": 5, "DEF": 1, "SPD": 4, "EXP": 8, "Gold": 5}
        damage = 5
        cure_hp(enemy_appeared, damage)
        expected = {"Name": "Dracula", "HP": 40, "STR": 5, "DEF": 1, "SPD": 4, "EXP": 8, "Gold": 5}
        self.assertEqual(expected, enemy_appeared)

    def test_dracula_hp_is_less_than_cured(self):
        enemy_appeared = {"Name": "Dracula", "HP": 20, "STR": 5, "DEF": 1, "SPD": 4, "EXP": 8, "Gold": 5}
        damage = 5
        cure_hp(enemy_appeared, damage)
        expected = {"Name": "Dracula", "HP": 25, "STR": 5, "DEF": 1, "SPD": 4, "EXP": 8, "Gold": 5}
        self.assertEqual(expected, enemy_appeared)

    def test_dracula_hp_is_exact_to_damage(self):
        enemy_appeared = {"Name": "Dracula", "HP": 35, "STR": 5, "DEF": 1, "SPD": 4, "EXP": 8, "Gold": 5}
        damage = 5
        cure_hp(enemy_appeared, damage)
        expected = {"Name": "Dracula", "HP": 40, "STR": 5, "DEF": 1, "SPD": 4, "EXP": 8, "Gold": 5}
        self.assertEqual(expected, enemy_appeared)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_oberon_hp_greater_than_to_30(self, mock_output):
        enemy_appeared = {"Name": "Dracula", "HP": 35, "STR": 5, "DEF": 1, "SPD": 4, "EXP": 8, "Gold": 5}
        damage = 5
        cure_hp(enemy_appeared, damage)
        expected = ("Dracula has sucked your blood! He recovered HP.\n"
                    f"Dracula now has {enemy_appeared['HP']} HP.\n\n")
        self.assertEqual(expected, mock_output.getvalue())
