import io
from unittest import TestCase
from unittest.mock import patch
from modules.battle.battle import summon_pixie


class TestSummonPixie(TestCase):
    def test_oberon_hp_greater_than_to_30(self):
        enemy_appeared = {"Name": "Oberon", "HP": 35, "STR": 4, "DEF": 0, "SPD": 6, "EXP": 8, "Gold": 5}
        summon_pixie(enemy_appeared)
        expected = {"Name": "Oberon", "HP": 40, "STR": 4, "DEF": 0, "SPD": 6, "EXP": 8, "Gold": 5}
        self.assertEqual(expected, enemy_appeared)

    def test_oberon_hp_is_30(self):
        enemy_appeared = {"Name": "Oberon", "HP": 30, "STR": 4, "DEF": 0, "SPD": 6, "EXP": 8, "Gold": 5}
        summon_pixie(enemy_appeared)
        expected = {"Name": "Oberon", "HP": 40, "STR": 4, "DEF": 0, "SPD": 6, "EXP": 8, "Gold": 5}
        self.assertEqual(expected, enemy_appeared)

    def test_oberon_hp_less_than_to_30(self):
        enemy_appeared = {"Name": "Oberon", "HP": 20, "STR": 4, "DEF": 0, "SPD": 6, "EXP": 8, "Gold": 5}
        summon_pixie(enemy_appeared)
        expected = {"Name": "Oberon", "HP": 30, "STR": 4, "DEF": 0, "SPD": 6, "EXP": 8, "Gold": 5}
        self.assertEqual(expected, enemy_appeared)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_oberon_hp_greater_than_to_30(self, mock_output):
        enemy_appeared = {"Name": "Oberon", "HP": 35, "STR": 4, "DEF": 0, "SPD": 6, "EXP": 8, "Gold": 5}
        summon_pixie(enemy_appeared)
        expected = (f"Oberon has summoned a High Pixie! The Pixie heals him for 10 HP.\n"
                    f"Oberon now has {enemy_appeared['HP']} HP.\n\n")
        self.assertEqual(expected, mock_output.getvalue())
