import unittest
from unittest import TestCase

from modules.battle.talk import get_reply_boss
from unittest.mock import patch


class TestGetReplyBoss(TestCase):
    def setUp(self) -> None:
        self.can_start = False
        self.enemy_appeared = {"Name": "Dracula", "HP": 40, "STR": 5, "DEF": 1, "SPD": 4, "EXP": 8, "Gold": 5}
        self.question = 'Question 1'
        self.specific_enemy_lines = {
            "Question 1":
                {"Question": "You wish to speak to me?!\nProve your worth. Let me taste your blood.",
                 "Answer 1": "Hmmm if it is the only way. (HP -20)",
                 "Answer 2": "I am weak please spare me!",
                 "Answer 3": "My blood tastes awful though...",
                 "Reply 1": "Blergh! tastes awful",
                 "Reply 1.1": "Hmm, not bad.",
                 "Reply 2": "I will spare you from this world!",
                 "Reply 2.1": "Hmph, I have no need for weakling blood anyways.",
                 "Reply 3": "I will be the one to decide that!",
                 "Reply 3.1": "True, you don't look particularly appetizing."}}
        self.response_options = {1: self.specific_enemy_lines[self.question]["Answer 1"],
                                 2: self.specific_enemy_lines[self.question]["Answer 2"],
                                 3: self.specific_enemy_lines[self.question]["Answer 3"]}

    def test_character_hp_is_zero(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 0, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        response = 1
        result = get_reply_boss(response, self.response_options, character_dictionary,
                                self.enemy_appeared, self.specific_enemy_lines, self.question)
        expected = False
        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=[1, 2])
    def test_response_to_answer_1(self, _):
        response = 1
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1000,
                                                     "DEF": 5, "CHR": 10, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        result = get_reply_boss(response, self.response_options, character_dictionary,
                                self.enemy_appeared, self.specific_enemy_lines, self.question)
        self.assertTrue(result)

    @patch('builtins.input', side_effect=[1, 2])
    def test_response_to_answer_2_not_enough_CHR(self, _):
        response = 2
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1000,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        with unittest.mock.patch('modules.battle.battle.fight_miniboss') as mock_fight_miniboss:
            get_reply_boss(response, self.response_options, character_dictionary,
                           self.enemy_appeared, self.specific_enemy_lines, self.question)
            mock_fight_miniboss.assert_called_with(character_dictionary, self.enemy_appeared)

    @patch('builtins.input', side_effect=[1, 2])
    def test_response_to_answer_2_enough_CHR(self, _):
        response = 2
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        result = get_reply_boss(response, self.response_options, character_dictionary,
                                self.enemy_appeared, self.specific_enemy_lines, self.question)
        self.assertFalse(result)

    def test_response_to_answer_3_not_enough_CHR(self):
        response = 3
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        with unittest.mock.patch('modules.battle.battle.fight_miniboss') as mock_fight_miniboss:
            get_reply_boss(response, self.response_options, character_dictionary,
                           self.enemy_appeared, self.specific_enemy_lines, self.question)
            mock_fight_miniboss.assert_called_with(character_dictionary, self.enemy_appeared)

    @patch('builtins.input', side_effect=[1, 2])
    def test_response_to_answer_3_enough_CHR(self, _):
        response = 3
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1000,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        result = get_reply_boss(response, self.response_options, character_dictionary,
                                self.enemy_appeared, self.specific_enemy_lines, self.question)
        self.assertFalse(result)
