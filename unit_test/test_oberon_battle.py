import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.battle.battle import oberon_turn


class TestOberonBattle(TestCase):
    def setUp(self) -> None:
        self.character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                          "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                     "Items": {"Gold": 0, "Potions": 0}}
        self.turn = "enemy"

    def test_rounds_is_3(self):
        with unittest.mock.patch('modules.battle.battle.summon_pixie') as mock_summon_pixie:
            enemy_appeared = {"Name": "Oberon", "HP": 40, "STR": 4, "DEF": 0, "SPD": 6, "EXP": 8, "Gold": 5}
            rounds = 3
            oberon_turn(self.character_dictionary, enemy_appeared, self.turn, rounds)
            mock_summon_pixie.assert_called_with(enemy_appeared)

    def test_rounds_is_not_3(self):
        with unittest.mock.patch('modules.battle.battle.enemy_turn') as mock_enemy_turn:
            enemy_appeared = {"Name": "Oberon", "HP": 40, "STR": 4, "DEF": 0, "SPD": 6, "EXP": 8, "Gold": 5}
            rounds = 2
            oberon_turn(self.character_dictionary, enemy_appeared, self.turn, rounds)
            mock_enemy_turn.assert_called_with(self.character_dictionary, enemy_appeared, self.turn)
