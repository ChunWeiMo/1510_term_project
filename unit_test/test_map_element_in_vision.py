from modules.exploration.vision import map_element_in_vision
from unittest import TestCase


class TestMapElementInVision(TestCase):
    def test_see_door(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 12, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 11, "VIS": 3},
                                "Name": "describe", "X-coordinate": 0, "Y-coordinate": 0,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        column = 1
        row = 1
        current_map = {(0, 0): "Empty", (1, 0): "Empty", (0, 1): "Empty", (1, 1): "Door"}
        expected_map_element = "Door"
        self.assertEqual(expected_map_element, map_element_in_vision(character_dictionary, current_map, column, row))

    def test_see_EW_wall(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 101, "STR": 12, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 11, "VIS": 3},
                                "Name": "describe", "X-coordinate": 0, "Y-coordinate": 0,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        column = -1
        row = 0
        current_map = {(0, 0): "Empty", (1, 0): "Empty", (0, 1): "Empty", (1, 1): "Door"}
        expected_map_element = "EW_wall"
        self.assertEqual(expected_map_element, map_element_in_vision(character_dictionary, current_map, column, row))

    def test_see_NS_wall(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 101, "STR": 12, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 11, "VIS": 3},
                                "Name": "describe", "X-coordinate": 0, "Y-coordinate": 0,
                                "EXP": 1, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        column = 0
        row = -1
        current_map = {(0, 0): "Empty", (1, 0): "Empty", (0, 1): "Empty", (1, 1): "Door"}
        expected_map_element = "NS_wall"
        self.assertEqual(expected_map_element, map_element_in_vision(character_dictionary, current_map, column, row))
