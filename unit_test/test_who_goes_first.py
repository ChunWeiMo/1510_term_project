from unittest import TestCase
from unittest.mock import patch

from modules.battle.battle import who_goes_first


class TestFirst(TestCase):
    def setUp(self):
        self.character_dictionary = {"Character_status": {"SPD": 10}}
    def test_enemy_speed_greater_than_character(self):
        enemy_appeared = {"SPD": 13}
        result = who_goes_first(self.character_dictionary, enemy_appeared)
        expected_turn = "enemy"
        self.assertEqual(expected_turn, result)

    def test_character_speed_greater_than_enemy(self):
        enemy_appeared = {"SPD": 4}
        result = who_goes_first(self.character_dictionary, enemy_appeared)
        expected_turn = "character"
        self.assertEqual(expected_turn, result)

    @patch('modules.battle.enemy.random.randint', return_value=2)
    def test_enemy_speed_equal_to_character_roll_2(self, _):
        enemy_appeared = {"SPD": 10}
        result = who_goes_first(self.character_dictionary, enemy_appeared)
        expected_turn = "enemy"
        self.assertEqual(expected_turn, result)

    @patch('modules.battle.enemy.random.randint', return_value=1)
    def test_character_speed_equal_to_enemy_roll_1(self, _):
        enemy_appeared = {"SPD": 10}
        result = who_goes_first(self.character_dictionary, enemy_appeared)
        expected_turn = "character"
        self.assertEqual(expected_turn, result)
