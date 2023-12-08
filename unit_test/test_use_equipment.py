from unittest import TestCase
from modules.character.equipment import use_equipment


class TestUseEquipment(TestCase):
    def test_have_no_equipment_before_use_equipment(self):
        character_dictionary = {
            "Character_status": {"Level": 1, "HP": 90, "STR": 11, "DEF": 5, "CHR": 5, "SPD": 5, "LUK": 5, "VIS": 2},
            "Equipment": 0}
        old_equipment = 0
        new_equipment = ["Cheat coin", ("LUK", 3)]
        use_equipment(character_dictionary, old_equipment, new_equipment)
        expected_character_dictionary = {
            "Character_status": {"Level": 1, "HP": 90, "STR": 11, "DEF": 5, "CHR": 5, "SPD": 5, "LUK": 8, "VIS": 2},
            "Equipment": ["Cheat coin", ("LUK", 3)]}
        self.assertEqual(expected_character_dictionary, character_dictionary)

    def test_replace_equipment_new_equipment_only_buff(self):
        character_dictionary = {
            "Character_status": {"Level": 2, "HP": 100, "STR": 18, "DEF": 5, "CHR": 5, "SPD": 5, "LUK": 5, "VIS": 2},
            "Equipment": ["Silver sword", ("STR", 7)]}
        old_equipment = ["Silver sword", ("STR", 7)]
        new_equipment = ["Platinum shield", ("DEF", 7)]
        use_equipment(character_dictionary, old_equipment, new_equipment)
        expected_character_dictionary = {
            "Character_status": {"Level": 2, "HP": 100, "STR": 11, "DEF": 12, "CHR": 5, "SPD": 5, "LUK": 5, "VIS": 2},
            "Equipment": ["Platinum shield", ("DEF", 7)]}
        self.assertEqual(expected_character_dictionary, character_dictionary)

    def test_replace_equipment_new_equipment_has_buff_and_debuff(self):
        character_dictionary = {
            "Character_status": {"Level": 1, "HP": 70, "STR": 18, "DEF": 5, "CHR": 5, "SPD": 5, "LUK": 5, "VIS": 2},
            "Equipment": ["Noble insignia", ("CHR", 3)]}
        old_equipment = ["Noble insignia", ("CHR", 3)]
        new_equipment = ["The lance of curses", ("STR", 6), ("HP", -30)]
        use_equipment(character_dictionary, old_equipment, new_equipment)
        expected_character_dictionary = {
            "Character_status": {"Level": 1, "HP": 40, "STR": 24, "DEF": 5, "CHR": 2, "SPD": 5, "LUK": 5, "VIS": 2},
            "Equipment": ["The lance of curses", ("STR", 6), ("HP", -30)]}
        self.assertEqual(expected_character_dictionary, character_dictionary)
