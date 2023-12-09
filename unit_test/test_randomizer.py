from unittest import TestCase
from unittest.mock import patch

from modules.battle.talk import randomizer


class TestRandomizer(TestCase):
    @patch('modules.battle.enemy.random.randint', return_value=1)
    def test_random_number_1(self, _):
        specific_enemy_lines = {
            "Question": "Plip plop plip plop~~",
            "Answer 1": "*Pat it*",
            "Answer 2": "*Squeeze it*",
            "Answer 3": "*kick it*",
            "Reply 1": "Pliippp! (it looks happy)",
            "Reply 2": "PLIPP! (battle)",
            "Reply 2.1": "Pliiiipppp~ (it looks content)",
            "Reply 3": "GRRrr (battle)",
            "Reply 3.1": "plip..(it looks sad and scared)"}
        result = randomizer(specific_enemy_lines)
        expected = {1: specific_enemy_lines["Answer 1"],
                    2: specific_enemy_lines["Answer 2"],
                    3: specific_enemy_lines["Answer 3"]}
        self.assertEqual(result, expected)

    @patch('modules.battle.enemy.random.randint', return_value=2)
    def test_random_number_2(self, _):
        specific_enemy_lines = {
            "Question": "Plip plop plip plop~~",
            "Answer 1": "*Pat it*",
            "Answer 2": "*Squeeze it*",
            "Answer 3": "*kick it*",
            "Reply 1": "Pliippp! (it looks happy)",
            "Reply 2": "PLIPP! (battle)",
            "Reply 2.1": "Pliiiipppp~ (it looks content)",
            "Reply 3": "GRRrr (battle)",
            "Reply 3.1": "plip..(it looks sad and scared)"}
        result = randomizer(specific_enemy_lines)
        expected = {3: specific_enemy_lines["Answer 1"],
                    1: specific_enemy_lines["Answer 2"],
                    2: specific_enemy_lines["Answer 3"]}
        self.assertEqual(result, expected)

    @patch('modules.battle.enemy.random.randint', return_value=3)
    def test_random_number_3(self, _):
        specific_enemy_lines = {
            "Question": "Plip plop plip plop~~",
            "Answer 1": "*Pat it*",
            "Answer 2": "*Squeeze it*",
            "Answer 3": "*kick it*",
            "Reply 1": "Pliippp! (it looks happy)",
            "Reply 2": "PLIPP! (battle)",
            "Reply 2.1": "Pliiiipppp~ (it looks content)",
            "Reply 3": "GRRrr (battle)",
            "Reply 3.1": "plip..(it looks sad and scared)"}
        result = randomizer(specific_enemy_lines)
        expected = {2: specific_enemy_lines["Answer 1"],
                    3: specific_enemy_lines["Answer 2"],
                    1: specific_enemy_lines["Answer 3"]}
        self.assertEqual(result, expected)
