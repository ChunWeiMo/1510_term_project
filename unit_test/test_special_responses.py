from unittest import TestCase

from modules.battle.talk import check_special_responses


class TestSpecialResponse(TestCase):
    def test_response_that_gives_player_potion(self):
        specific_enemy_lines = {
            "Reply 2.1": "How's a potion sound?"}
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        check_special_responses(specific_enemy_lines, character_dictionary)
        expected = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                         "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                    "Items": {"Gold": 0, "Potions": 1}}
        self.assertEqual(expected, character_dictionary)

    def test_response_that_gives_player_gold(self):
        specific_enemy_lines = {
            "Reply 2.1": "Whaddup",
            "Reply 3.1": "EEEK! Yessir! (+5 Gold)"}
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        check_special_responses(specific_enemy_lines, character_dictionary)
        expected = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                         "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                    "Items": {"Gold": 5, "Potions": 0}}
        self.assertEqual(expected, character_dictionary)
