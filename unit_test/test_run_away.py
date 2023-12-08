from unittest import TestCase
import io
from unittest.mock import patch
from modules.battle.battle import run_away


class TestRunAway(TestCase):
    def setUp(self):
        self.character_dictionary = {"Character_status": {"SPD": 10, "LUK": 5}}

    @patch('modules.battle.enemy.random.randint', return_value=30)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_run_away_successful(self, mock_output, _):
        run_away(self.character_dictionary)
        expected = "Successfully escaped!\n\n"
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('modules.battle.enemy.random.randint', return_value=30)
    def test_run_away_successful(self, _):
        result = run_away(self.character_dictionary)
        expected = True
        (self.assertEqual(result, expected))

    @patch('modules.battle.enemy.random.randint', return_value=80)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_run_away_failed(self, mock_output, _):
        run_away(self.character_dictionary)
        expected = "You failed to escape...prepare to engage in battle!\n\n"
        (self.assertEqual(mock_output.getvalue(), expected))

    @patch('modules.battle.enemy.random.randint', return_value=80)
    def test_run_away_failed(self, _):
        result = run_away(self.character_dictionary)
        expected = False
        (self.assertEqual(result, expected))
