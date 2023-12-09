import json
import os
from unittest import TestCase
from modules.menu.saveload import loaddata


class TestLoadData(TestCase):
    def setUp(self):
        self.character_dictionary = {"name": "AAAA"}

    def test_loaddata_succefully(self):
        current_map = {"(0, 0)": "Empty", "(1, 0)": "Empty", "(2, 0)": "Empty"}
        with open("./character.json", "w") as file_object:
            json.dump(self.character_dictionary, file_object)
        with open("./current_map.json", 'w') as file_object:
            json.dump(current_map, file_object)
        character_dictionary, current_map = loaddata()
        self.assertEqual(self.character_dictionary, character_dictionary)
        self.assertEqual(current_map, current_map)
        if os.path.exists("./character.json"):
            os.remove("./character.json")
        if os.path.exists("./current_map.json"):
            os.remove("./current_map.json")

    def test_loaddata_failed(self):
        result = loaddata()
        if result is not None:
            self.fail("FileNotFoundError was expected but not raised.")
        else:
            self.assertIsNone(result)
