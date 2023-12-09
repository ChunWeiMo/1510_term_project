import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.menu.saveload import ask_loaddata


class TestAskLoadData(TestCase):
    def setUp(self):
        self.character_dictionary = {"name": "AAAA"}
        self.current_map = {"(0, 0)": "Empty", "(1, 0)": "Empty", "(2, 0)": "Empty"}

    @patch('builtins.input', side_effect=['Y'])
    def test_input_Y_to_load_savedata(self, _):
        with unittest.mock.patch('modules.menu.saveload.loaddata') as mock_loaddata:
            mock_loaddata.return_value = ({"name": "AAAA"}, {"(0, 0)": "Empty", "(1, 0)": "Empty", "(2, 0)": "Empty"})
            character_dictionary, current_map = ask_loaddata(self.character_dictionary, self.current_map)
            self.assertEqual(self.character_dictionary, character_dictionary)
            self.assertEqual(self.current_map, current_map)
            mock_loaddata.assert_called_once()

    @patch('builtins.input', side_effect=['N'])
    def test_input_other_not_load_savedata(self, _):
        expected_character_dictionary = self.character_dictionary
        expected_current_map = self.current_map
        self.assertEqual((expected_character_dictionary, expected_current_map),
                         ask_loaddata(self.character_dictionary, self.current_map))
