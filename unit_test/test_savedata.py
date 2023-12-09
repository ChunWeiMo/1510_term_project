import os
from unittest import TestCase
from modules.menu.saveload import savedata


class TestSaveDate(TestCase):
    def setUp(self):
        self.character_dictionary = {"name": "AAAA"}

    def test_savedata_succefully(self):
        current_map = {"(0, 0)": "Empty", "(1, 0)": "Empty", "(2, 0)": "Empty"}
        savedata(self.character_dictionary, current_map)
        self.assertTrue(os.path.exists("./character.json"))
        self.assertTrue(os.path.exists("./current_map.json"))
        if os.path.exists("./character.json"):
            os.remove("./character.json")
        if os.path.exists("./current_map.json"):
            os.remove("./current_map.json")

    def test_current_map_not_dict_raise_TypeError(self):
        current_map = "current_map"
        with self.assertRaises(TypeError):
            savedata(self.character_dictionary, current_map)
