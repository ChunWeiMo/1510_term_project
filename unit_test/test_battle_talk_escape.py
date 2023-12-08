import io
import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.battle.enemy import battle_talk_escape


class TestBTE(TestCase):
    def setUp(self):
        self.character_dictionary = {'Character_status': {'HP': 50, 'STR': 10, 'DEF': 5, "SPD": 1, "LUK": 1}}
        self.can_start = True

    def test_input_1_battle_regular_enemy(self):
        with unittest.mock.patch('modules.battle.battle.fight') as mock_fight:
            enemy_appeared = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
            user_input = 1
            battle_talk_escape(self.character_dictionary, user_input, enemy_appeared)
            mock_fight.assert_called_with(self.character_dictionary, enemy_appeared, self.can_start)

    def test_input_1_battle_miniboss(self):
        with unittest.mock.patch('modules.battle.battle.fight_miniboss') as mock_fight_miniboss:
            enemy_appeared = {"Name": "Cerberus", "HP": 50, "STR": 5, "DEF": 5, "SPD": 0, "EXP": 8, "Gold": 5}
            user_input = 1
            battle_talk_escape(self.character_dictionary, user_input, enemy_appeared)
            mock_fight_miniboss.assert_called_with(self.character_dictionary, enemy_appeared)

    def test_input_1_battle_final_boss(self):
        with unittest.mock.patch('modules.battle.battle.fight_final_boss') as mock_fight_final_boss:
            enemy_appeared = {"Name": "Evil Dragon", "HP": 100, "STR": 7, "DEF": 4, "SPD": 3, "EXP": 0, "Gold": 0}
            user_input = 1
            battle_talk_escape(self.character_dictionary, user_input, enemy_appeared)
            mock_fight_final_boss.assert_called_with(self.character_dictionary, enemy_appeared)

    def test_input_2_talk_regular(self):
        with unittest.mock.patch('modules.battle.talk.talk_to_enemy') as mock_talk_to_enemy:
            enemy_appeared = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
            user_input = 2
            battle_talk_escape(self.character_dictionary, user_input, enemy_appeared)
            mock_talk_to_enemy.assert_called_with(self.character_dictionary, enemy_appeared)

    def test_talk_input_2_miniboss(self):
        with unittest.mock.patch('modules.battle.talk.talk_to_enemy') as mock_talk_to_enemy:
            enemy_appeared = {"Name": "Cerberus", "HP": 50, "STR": 5, "DEF": 5, "SPD": 0, "EXP": 8, "Gold": 5}
            user_input = 2
            battle_talk_escape(self.character_dictionary, user_input, enemy_appeared)
            mock_talk_to_enemy.assert_called_with(self.character_dictionary, enemy_appeared)

    def test_talk_input_2_final_boss(self):
        with unittest.mock.patch('modules.battle.talk.talk_to_enemy') as mock_talk_to_enemy:
            enemy_appeared = {"Name": "Evil Dragon", "HP": 100, "STR": 7, "DEF": 4, "SPD": 3, "EXP": 0, "Gold": 0}
            user_input = 2
            battle_talk_escape(self.character_dictionary, user_input, enemy_appeared)
            mock_talk_to_enemy.assert_called_with(self.character_dictionary, enemy_appeared)

    @patch('builtins.input', side_effect=[1])
    def test_input_3_use_potion(self, _):
        with unittest.mock.patch('modules.character.items.use_potion') as mock_use_potion:
            enemy_appeared = {"Name": "Evil Dragon", "HP": 100, "STR": 7, "DEF": 4, "SPD": 3, "EXP": 0, "Gold": 0}
            user_input = 3
            battle_talk_escape(self.character_dictionary, user_input, enemy_appeared)
            mock_use_potion.assert_called_with(self.character_dictionary)

    def test_input_4_can_run_away(self):
        with unittest.mock.patch('modules.battle.battle.run_away') as mock_run_away:
            enemy_appeared = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
            user_input = 4
            battle_talk_escape(self.character_dictionary, user_input, enemy_appeared)
            mock_run_away.assert_called_with(self.character_dictionary)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[1])
    def test_input_4_cannot_run_from_dragon(self, _, mock_output):
        enemy_appeared = {"Name": "Evil Dragon", "HP": 100, "STR": 7, "DEF": 4, "SPD": 3, "EXP": 0, "Gold": 0}
        user_input = 4
        battle_talk_escape(self.character_dictionary, user_input, enemy_appeared)
        expected = "You cannot run away from Evil Dragon!\nEvil Dragon appears before you!\n"
        self.assertEqual(mock_output.getvalue(), expected)

    def test_input_4_fail_to_run(self):
        with unittest.mock.patch('modules.battle.battle.fight') as mock_fight:
            enemy_appeared = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
            user_input = 4
            battle_talk_escape(self.character_dictionary, user_input, enemy_appeared)
            can_run = False
            can_start = False
            mock_fight.assert_called_with(self.character_dictionary, enemy_appeared, can_start)
