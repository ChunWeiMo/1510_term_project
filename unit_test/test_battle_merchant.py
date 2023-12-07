from unittest import TestCase
from modules.character.items import battle_merchant


class TestBattleMerchant(TestCase):

    def setUp(self):
        self.character_dictionary = {
            'Character_status': {'HP': 50, 'STR': 10, 'DEF': 5}}

    def test_character_dies(self):
        battle_merchant(self.character_dictionary)
        expected = {'Character_status': {'HP': -40, 'STR': 10, 'DEF': 5}}
        self.assertEqual(expected, self.character_dictionary)

    def test_merchant_dies(self):
        character_dictionary = {
            'Character_status': {'HP': 5000, 'STR': 9999, 'DEF': 5}}
        battle_merchant(character_dictionary)
        expected = {'Character_status': {'DEF': 5, 'HP': 4910, 'STR': 9999}}
        self.assertEqual(expected, character_dictionary)
