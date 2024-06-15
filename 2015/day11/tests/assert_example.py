import unittest
from models.corporate_password import CorporatePassword


class TestFunction(unittest.TestCase):
    def test_valid_password(self):
        self.assertEqual(CorporatePassword("hijklmmn").is_valid_password(), False) # noqa
        self.assertEqual(CorporatePassword("abbceffg").is_valid_password(), False) # noqa
        self.assertEqual(CorporatePassword("abbcegjk").is_valid_password(), False) # noqa
        self.assertEqual(CorporatePassword("abcdefgh").is_valid_password(), False) # noqa
        self.assertEqual(CorporatePassword("ghijklmn").is_valid_password(), False) # noqa
        self.assertEqual(CorporatePassword("abcdffaa").is_valid_password(), True) # noqa
        self.assertEqual(CorporatePassword("ghjaabcc").is_valid_password(), True) # noqa

    def test_inrement_password(self):
        self.assertEqual(CorporatePassword("hijklmmn").increment_password(), 'hijklmmo') # noqa
        self.assertEqual(CorporatePassword("hijklmmz").increment_password(), 'hijklmna') # noqa
        self.assertEqual(CorporatePassword("hzzzzzzz").increment_password(), 'iaaaaaaa') # noqa
