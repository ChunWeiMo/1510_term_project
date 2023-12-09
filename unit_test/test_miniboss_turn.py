import unittest
from unittest import TestCase
from unittest.mock import patch

from modules.battle.battle import miniboss_turn


class TestMinibossTurn(TestCase):
    def setUp(self) -> None:
        self.character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                          "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                     "Items": {"Gold": 0, "Potions": 0}}
        self.turn = "enemy"
        self.rounds = 1

    def test_enemy_appeared_is_oberon(self):
        with unittest.mock.patch('modules.battle.battle.oberon_turn') as mock_oberon_turn:
            enemy_appeared = {"Name": "Oberon", "HP": 40, "STR": 4, "DEF": 0, "SPD": 6, "EXP": 8, "Gold": 5}
            rounds = 1
            miniboss_turn(self.character_dictionary, enemy_appeared, self.turn, rounds)
            mock_oberon_turn.assert_called_with(self.character_dictionary, enemy_appeared, self.turn, self.rounds)

    def test_enemy_appeared_is_cerberus(self):
        with unittest.mock.patch('modules.battle.battle.cerberus_turn') as mock_cerberus_turn:
            enemy_appeared = {"Name": "Cerberus", "HP": 50, "STR": 5, "DEF": 5, "SPD": 0, "EXP": 8, "Gold": 5}
            miniboss_turn(self.character_dictionary, enemy_appeared, self.turn, self.rounds)
            mock_cerberus_turn.assert_called_with(self.character_dictionary, enemy_appeared)

    def test_enemy_appeared_is_dracula(self):
        with unittest.mock.patch('modules.battle.battle.dracula_turn') as mock_dracula_turn:
            enemy_appeared = {"Name": "Dracula", "HP": 40, "STR": 5, "DEF": 1, "SPD": 4, "EXP": 8, "Gold": 5}
            miniboss_turn(self.character_dictionary, enemy_appeared, self.turn, self.rounds)
            mock_dracula_turn.assert_called_with(self.character_dictionary, enemy_appeared)
