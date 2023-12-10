from modules.exploration.movement import check_for_event
from unittest import TestCase, mock
from unittest.mock import patch
import io


class TestCheckForEvent(TestCase):
    @mock.patch('modules.exploration.event.encounter_final_boss')
    def test_not_meet_final_boss_on_empty(self, mock_encounter_final_boss):
        character_dictionary = {"X-coordinate": 1, "Y-coordinate": 1}
        current_map = {(1, 1): "Empty"}
        check_for_event(character_dictionary, current_map)
        mock_encounter_final_boss.assert_not_called()

    @mock.patch('modules.exploration.event.encounter_an_enemy')
    def test_not_meet_enemy_on_empty(self, mock_encounter_an_enemy):
        character_dictionary = {"X-coordinate": 1, "Y-coordinate": 1}
        current_map = {(1, 1): "Empty"}
        check_for_event(character_dictionary, current_map)
        mock_encounter_an_enemy.assert_not_called()

    @mock.patch('modules.exploration.event.encounter_merchant')
    def test_not_meet_merchant_on_empty(self, mock_encounter_merchant):
        character_dictionary = {"X-coordinate": 1, "Y-coordinate": 1}
        current_map = {(1, 1): "Empty"}
        check_for_event(character_dictionary, current_map)
        mock_encounter_merchant.assert_not_called()

    @mock.patch('modules.exploration.event.find_a_chest')
    def test_not_find_chest_on_empty(self, mock_find_a_chest):
        character_dictionary = {"X-coordinate": 1, "Y-coordinate": 1}
        current_map = {(1, 1): "Empty"}
        check_for_event(character_dictionary, current_map)
        mock_find_a_chest.assert_not_called()

    @patch('random.randint', side_effect=[1, 1])
    @patch('builtins.input', side_effect=["4"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_meet_Enemy_Slime(self, mock_output, _, __):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 2, "SPD": 1,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 2, "Y-coordinate": 1,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(0, 0): "Empty", (1, 0): "Empty", (2, 0): "Empty",
                       (1, 0): "Empty", (1, 1): "Empty", (2, 1): "Enemy"}
        check_for_event(character_dictionary, current_map)
        expected_message = "You meet Enemy!\n\nSlime appears before you!\nSuccessfully escaped!\n\n"
        self.assertEqual(expected_message, mock_output.getvalue())

    @patch('random.randint', side_effect=[1, 1])
    @patch('builtins.input', side_effect=["4"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_meet_Enemy_Cave_Spider(self, mock_output, _, __):
        character_dictionary = {"Character_status": {"Level": 2, "HP": 100, "STR": 11, "DEF": 1, "CHR": 2, "SPD": 1,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 1, "Y-coordinate": 1,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(0, 0): "Empty", (1, 0): "Empty", (2, 0): "Empty",
                       (1, 0): "Empty", (1, 1): "Enemy", (2, 1): "Empty"}
        check_for_event(character_dictionary, current_map)
        expected_message = "You meet Enemy!\n\nCave Spider appears before you!\nSuccessfully escaped!\n\n"
        self.assertEqual(expected_message, mock_output.getvalue())

    @patch('builtins.input', side_effect=["N"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_meet_Door(self, mock_output, _):
        character_dictionary = {"Character_status": {"Level": 2, "HP": 100, "STR": 11, "DEF": 1, "CHR": 2, "SPD": 5,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 1, "Y-coordinate": 1,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(0, 0): "Empty", (1, 0): "Empty", (2, 0): "Empty",
                       (1, 0): "Empty", (1, 1): "Door", (2, 1): "Empty"}
        check_for_event(character_dictionary, current_map)
        expected_message = "You meet Door!\n\nMaybe there is still something to explore here?\n"
        self.assertEqual(expected_message, mock_output.getvalue())

    @patch('random.randint', side_effect=[1, 1])
    @patch('builtins.input', side_effect=["4"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_meet_Oberon(self, mock_output, _, __):
        character_dictionary = {"Character_status": {"Level": 2, "HP": 100, "STR": 11, "DEF": 10, "CHR": 2, "SPD": 5,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 1, "Y-coordinate": 1,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(0, 0): "Empty", (1, 0): "Empty", (2, 0): "Empty",
                       (1, 0): "Empty", (1, 1): "Oberon", (2, 1): "Empty"}
        check_for_event(character_dictionary, current_map)
        expected_message = "You meet Oberon!\n\nOberon appears before you!\nSuccessfully escaped!\n\n"
        self.assertEqual(expected_message, mock_output.getvalue())

    @patch('random.randint', side_effect=[1, 1])
    @patch('builtins.input', side_effect=["4"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_meet_Cerberus(self, mock_output, _, __):
        character_dictionary = {"Character_status": {"Level": 2, "HP": 90, "STR": 11, "DEF": 10, "CHR": 2, "SPD": 5,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 1, "Y-coordinate": 1,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(0, 0): "Empty", (1, 0): "Empty", (2, 0): "Empty",
                       (1, 0): "Empty", (1, 1): "Cerberus", (2, 1): "Empty"}
        check_for_event(character_dictionary, current_map)
        expected_message = "You meet Cerberus!\n\nCerberus appears before you!\nSuccessfully escaped!\n\n"
        self.assertEqual(expected_message, mock_output.getvalue())

    @patch('random.randint', side_effect=[1, 1])
    @patch('builtins.input', side_effect=["4"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_meet_Dracula(self, mock_output, _, __):
        character_dictionary = {"Character_status": {"Level": 2, "HP": 90, "STR": 31, "DEF": 10, "CHR": 2, "SPD": 5,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "describe", "X-coordinate": 1, "Y-coordinate": 1,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(0, 0): "Empty", (1, 0): "Empty", (2, 0): "Empty",
                       (1, 0): "Empty", (1, 1): "Dracula", (2, 1): "Empty"}
        check_for_event(character_dictionary, current_map)
        expected_message = "You meet Dracula!\n\nDracula appears before you!\nSuccessfully escaped!\n\n"
        self.assertEqual(expected_message, mock_output.getvalue())

    def test_meet_final_boss(self):
        character_dictionary = {
            "Character_status": {"Level": 3, "HP": 90, "STR": 500, "DEF": 100, "CHR": 2, "SPD": 100, "LUK": 1,
                                 "VIS": 3},
            "Name": "describe", "X-coordinate": 1, "Y-coordinate": 1,
            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
            "Equipment": 0, "Debuff": {"Burn": 0}
        }
        current_map = {(0, 0): "Empty", (1, 0): "Empty", (2, 0): "Empty",
                       (1, 0): "Empty", (1, 1): "Final Boss", (2, 1): "Empty"}

        with patch('modules.exploration.event.encounter_final_boss') as mock_encounter_final_boss:
            check_for_event(character_dictionary, current_map)
            mock_encounter_final_boss.assert_called_with(character_dictionary, current_map)

    @patch('random.randint', side_effect=[1, 1])
    @patch('builtins.input', side_effect=["4"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_meet_chest(self, mock_output, _, __):
        character_dictionary = {"Character_status": {"Level": 2, "HP": 90, "STR": 31, "DEF": 10, "CHR": 2, "SPD": 5,
                                                     "LUK": 10, "VIS": 3},
                                "Name": "describe", "X-coordinate": 1, "Y-coordinate": 1,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(0, 0): "Empty", (1, 0): "Empty", (2, 0): "Empty",
                       (1, 0): "Empty", (1, 1): "Chest", (2, 1): "Empty"}
        check_for_event(character_dictionary, current_map)
        expected_message = ("You meet Chest!\n\nSweet...You find Silver sword!\nThe ability of Silver sword:\nSTR 7\n\n"
                            "\n")
        self.assertEqual(expected_message, mock_output.getvalue())

    @patch('random.randint', side_effect=[1, 1])
    @patch('builtins.input', side_effect=["3"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_meet_Merchant(self, mock_output, _, __):
        character_dictionary = {"Character_status": {"Level": 2, "HP": 80, "STR": 31, "DEF": 10, "CHR": 2, "SPD": 5,
                                                     "LUK": 10, "VIS": 3},
                                "Name": "describe", "X-coordinate": 1, "Y-coordinate": 1,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(0, 0): "Empty", (1, 0): "Empty", (2, 0): "Empty",
                       (1, 0): "Empty", (1, 1): "Merchant", (2, 1): "Empty"}
        check_for_event(character_dictionary, current_map)
        expected_message = ("You meet Merchant!\n\n\nMerchant: Oh! What are you doing here? You must be a hero!\n"
                            "Come check out my humble store!\n\nMerchant: Thanks for stopping by!\n")
        self.assertEqual(expected_message, mock_output.getvalue())

    @patch('random.randint', side_effect=[1, 1])
    @patch('builtins.input', side_effect=["3"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_meet_Healing_fountain(self, mock_output, _, __):
        character_dictionary = {"Character_status": {"Level": 2, "HP": 80, "STR": 31, "DEF": 10, "CHR": 2, "SPD": 5,
                                                     "LUK": 9, "VIS": 3},
                                "Name": "describe", "X-coordinate": 1, "Y-coordinate": 1,
                                "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(0, 0): "Empty", (1, 0): "Empty", (2, 0): "Empty",
                       (1, 0): "Empty", (1, 1): "Healing_fountain", (2, 1): "Empty"}
        check_for_event(character_dictionary, current_map)
        expected_message = ("You meet Healing_fountain!\n\nTake a sip of water, for rest is meant to pave the way for "
                            "a longer journey ahead.\nYou get heal, HP +5\n")
        self.assertEqual(expected_message, mock_output.getvalue())
