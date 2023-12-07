from unittest import TestCase
from unittest.mock import patch
import io
from modules.character.items import leave_merchant


@patch('sys.stdout', new_callable=io.StringIO)
class TestLeaveMerchant(TestCase):
    def test_leave_merchant(self, mock_output):
        leave_merchant()
        expected = '\nMerchant: Thanks for stopping by!\n'
        self.assertEqual(expected, mock_output.getvalue())
