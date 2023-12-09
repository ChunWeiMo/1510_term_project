from unittest import TestCase
from modules.battle.battle import fight_final_boss


class TestFinalBoss(TestCase):
    def test_boss_hp_is_zero(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}, "Debuff": {"Burn": 0}}
        enemy_appeared = {"Name": "Evil Dragon", "HP": 0, "STR": 7, "DEF": 4, "SPD": 3, "EXP": 10, "Gold": 10}
        result = fight_final_boss(character_dictionary, enemy_appeared)
        expected = True
        self.assertEqual(result, expected)

    def test_character_hp_is_zero(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 0, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}, "Debuff": {"Burn": 0}}
        enemy_appeared = {"Name": "Evil Dragon", "HP": 100, "STR": 7, "DEF": 4, "SPD": 3, "EXP": 10, "Gold": 10}
        result = fight_final_boss(character_dictionary, enemy_appeared)
        expected = None
        self.assertEqual(result, expected)
