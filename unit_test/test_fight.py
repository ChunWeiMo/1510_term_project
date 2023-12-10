from unittest import TestCase

from modules.battle.battle import fight


class TestFight(TestCase):
    def test_enemy_hp_is_zero(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        enemy_appeared = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
        can_start = False
        result = fight(character_dictionary, enemy_appeared, can_start)
        expected = True
        self.assertEqual(result, expected)

    def test_character_hp_is_zero(self):
        character_dictionary = {"Character_status": {"HP": 0}}
        enemy_appeared = {"HP": 20}
        can_start = False
        result = fight(character_dictionary, enemy_appeared, can_start)
        expected = False
        self.assertEqual(result, expected)
