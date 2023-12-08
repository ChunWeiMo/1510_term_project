import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.battle.enemy import battle_talk_escape


class TestBTE(TestCase):
    def setUp(self):
        self.character_dictionary = {'Character_status': {'HP': 50, 'STR': 10, 'DEF': 5}}
        self.can_start = True

    def test_battle_regular(self):
        enemy_appeared = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
        user_input = 1
        with unittest.mock.patch('modules.battle.battle.fight') as mock_fight:
            battle_talk_escape(self.character_dictionary, enemy_appeared, user_input)
            mock_fight.assert_called_with(self.character_dictionary, enemy_appeared, self.can_start)

    def test_battle_miniboss(self):
        enemy_appeared = {"Name": "Cerberus"}
        user_input = 1
        with unittest.mock.patch('modules.battle.battle.fight') as mock_fight:
            battle_talk_escape(self.character_dictionary, enemy_appeared, user_input)
            mock_fight.assert_called_with(self.character_dictionary, enemy_appeared, self.can_start)

    def test_battle_final_boss(self):
        with unittest.mock.patch('modules.battle.battle.fight') as mock_fight:
            enemy_appeared = {"Name": "Evil Dragon"}
            user_input = 1
            battle_talk_escape(self.character_dictionary, user_input, enemy_appeared)
            mock_fight.assert_called_with(self.character_dictionary, enemy_appeared, self.can_start)

    def test_talk_regular(self):
        self.fail()

    def test_talk_miniboss(self):
        self.fail()

    def test_talk_final_boss(self):
        self.fail()

    def test_use_potion(self):
        self.fail()

    def test_can_run_away(self):
        self.fail()

    def test_cannot_run(self):
        self.fail()

    def test_fail_to_run(self):
        self.fail()

