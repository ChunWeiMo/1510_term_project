from unittest import TestCase
from unittest.mock import patch

from modules.battle.talk import randomizer, randomizer_boss


class TestRandomizer(TestCase):
    def setUp(self) -> None:
        self.specific_enemy_lines = {
            "Question 1":
                {"Question": "Why does cerberus have 3 heads?",
                 "Answer 1": "Because it makes you 3 times smarter!",
                 "Answer 2": "So you can eat 3 times as much!",
                 "Answer 3": "Because you are lonely?"},
            "Question 2":
                {"Question": "What is cerberus' favourite food?",
                 "Answer 1": "Human flesh.",
                 "Answer 2": "Cheeseburgers.",
                 "Answer 3": "Kibbles 'N Bits!"},
            "Question 3":
                {"Question": "How old do you think cerberus is?",
                 "Answer 1": "You look very wise and knowledgeable so you must be over 500!",
                 "Answer 2": "Your fur is so shiny and thick, you must be under 100!",
                 "Answer 3": "It is hard to tell since you are so well kept and majestic looking."}}

    @patch('modules.battle.enemy.random.randint', return_value=1)
    def test_random_number_1(self, _):
        question = "Question 1"
        result = randomizer_boss(self.specific_enemy_lines, question)
        expected = {1: self.specific_enemy_lines[question]["Answer 1"],
                    2: self.specific_enemy_lines[question]["Answer 2"],
                    3: self.specific_enemy_lines[question]["Answer 3"]}
        self.assertEqual(result, expected)

    @patch('modules.battle.enemy.random.randint', return_value=2)
    def test_random_number_2(self, _):
        question = "Question 2"
        result = randomizer_boss(self.specific_enemy_lines, question)
        expected = {3: self.specific_enemy_lines[question]["Answer 1"],
                    1: self.specific_enemy_lines[question]["Answer 2"],
                    2: self.specific_enemy_lines[question]["Answer 3"]}
        self.assertEqual(result, expected)

    @patch('modules.battle.enemy.random.randint', return_value=3)
    def test_random_number_3(self, _):
        question = "Question 3"
        result = randomizer_boss(self.specific_enemy_lines, question)
        expected = {2: self.specific_enemy_lines[question]["Answer 1"],
                    3: self.specific_enemy_lines[question]["Answer 2"],
                    1: self.specific_enemy_lines[question]["Answer 3"]}
        self.assertEqual(result, expected)
