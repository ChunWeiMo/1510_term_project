import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.battle.talk import get_chat_response


class TestGetChatResponse(TestCase):
    @patch('builtins.input', side_effect=[9, 3])
    def test_player_numeric_input_greater_than_max(self, _):
        response_options = {2: "test response 1",
                            3: "test response 2",
                            1: "test response 3"}
        response = get_chat_response(response_options)
        expected = 3
        self.assertEqual(expected, response)

    @patch('builtins.input', side_effect=[-3, 3])
    def test_player_numeric_input_less_than_max(self, _):
        response_options = {2: "test response 1",
                            3: "test response 2",
                            1: "test response 3"}
        response = get_chat_response(response_options)
        expected = 3
        self.assertEqual(expected, response)

    @patch('builtins.input', side_effect=['a', 3])
    def test_player_incorrect_alphabetical_input(self, _):
        response_options = {2: "test response 1",
                            3: "test response 2",
                            1: "test response 3"}
        response = get_chat_response(response_options)
        expected = 3
        self.assertEqual(expected, response)

    @patch('builtins.input', side_effect=['a', 1])
    def test_player_incorrect_alphabetical_input_value_error(self, _):
        response_options = {2: "test response 1",
                            3: "test response 2",
                            1: "test response 3"}
        get_chat_response(response_options)
        self.assertRaises(ValueError)