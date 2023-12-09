import unittest
from unittest import TestCase
from unittest.mock import patch

from modules.battle.talk import get_reply


class TestGetReplyFunction(TestCase):
    def setUp(self) -> None:
        self.can_start = False
        self.response_options = {1: "*Pat it*", 2: "*Squeeze it*", 3: "*kick it*"}
        self.enemy_appeared = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
        self.specific_enemy_lines = {
            "Question": "Plip plop plip plop~~",
            "Answer 1": "*Pat it*",
            "Answer 2": "*Squeeze it*",
            "Answer 3": "*kick it*",
            "Reply 1": "Pliippp! (it looks happy)",
            "Reply 2": "PLIPP! (battle)",
            "Reply 2.1": "Pliiiipppp~ (it looks content)",
            "Reply 3": "GRRrr (battle)",
            "Reply 3.1": "plip..(it looks sad and scared)"}

    def test_character_hp_is_zero(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 0, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        response = 1
        result = get_reply(response, self.response_options, character_dictionary,
                           self.enemy_appeared, self.specific_enemy_lines)
        expected = False
        self.assertEqual(result, expected)

    def test_response_to_answer_1(self):
        response = 1
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        result = get_reply(response, self.response_options, character_dictionary,
                           self.enemy_appeared, self.specific_enemy_lines)
        self.assertTrue(result)

    def test_response_to_answer_2_not_enough_CHR(self):
        response = 2
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        with unittest.mock.patch('modules.battle.battle.fight') as mock_fight:
            get_reply(response, self.response_options, character_dictionary,
                      self.enemy_appeared, self.specific_enemy_lines)
            mock_fight.assert_called_with(character_dictionary, self.enemy_appeared, self.can_start)

    def test_response_to_answer_2_enough_CHR(self):
        response = 2
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 5, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        result = get_reply(response, self.response_options, character_dictionary,
                           self.enemy_appeared, self.specific_enemy_lines)
        self.assertTrue(result)

    def test_response_to_answer_3_not_enough_CHR(self):
        response = 3
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        with unittest.mock.patch('modules.battle.battle.fight') as mock_fight:
            get_reply(response, self.response_options, character_dictionary,
                      self.enemy_appeared, self.specific_enemy_lines)
            mock_fight.assert_called_with(character_dictionary, self.enemy_appeared, self.can_start)

    def test_response_to_answer_3_enough_CHR(self):
        response = 3
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 7, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        result = get_reply(response, self.response_options, character_dictionary,
                           self.enemy_appeared, self.specific_enemy_lines)
        self.assertTrue(result)
