import unittest
from unittest import TestCase
from unittest.mock import patch

from modules.battle.battle import boss_turn


class TestBossTurn(TestCase):
    def setUp(self):
        self.character_dictionary = {"Character_status": {"Level": 1, "HP": 5, "STR": 1, "DEF": 5,
                                                     "CHR": 1, "SPD": 1, "LUK": 1}, "Debuff": {"Burn": 3}}
        self.enemy_appeared = {"Name": "Evil Dragon", "HP": 100, "STR": 7, "DEF": 4, "SPD": 3, "EXP": 10, "Gold": 10}
        self.turn = "enemy"

    @patch('modules.battle.enemy.random.randint', return_value=1)
    def test_random_number_1(self, _):
        with unittest.mock.patch('modules.battle.battle.enemy_turn') as mock_enemy_turn:
            boss_turn(self.character_dictionary, self.enemy_appeared, self.turn)
            mock_enemy_turn.assert_called_with(self.character_dictionary, self.enemy_appeared, self.turn)


    @patch('modules.battle.enemy.random.randint', return_value=2)
    def test_random_number_2(self, _):
        with unittest.mock.patch('modules.battle.battle.boss_fireball') as mock_boss_fireball:
            boss_turn(self.character_dictionary, self.enemy_appeared, self.turn)
            mock_boss_fireball.assert_called_with(self.character_dictionary, self.enemy_appeared)

    @patch('modules.battle.enemy.random.randint', return_value=3)
    def test_random_number_3(self, _):
        with unittest.mock.patch('modules.battle.battle.boss_tailwhip') as mock_boss_tailwhip:
            boss_turn(self.character_dictionary, self.enemy_appeared, self.turn)
            mock_boss_tailwhip.assert_called_with(self.character_dictionary, self.enemy_appeared)

    @patch('modules.battle.enemy.random.randint', return_value=4)
    def test_random_number_4(self, _):
        with unittest.mock.patch('modules.battle.battle.boss_claw_attack') as mock_boss_claw_attack:
            boss_turn(self.character_dictionary, self.enemy_appeared, self.turn)
            mock_boss_claw_attack.assert_called_with(self.character_dictionary, self.enemy_appeared)
