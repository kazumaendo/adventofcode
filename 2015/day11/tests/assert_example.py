import unittest
from models.corporate_password import CorporatePassword


class TestFunction(unittest.TestCase):
    def test_valid_password(self):
        self.assertEqual(CorporatePassword("hijklmmn"), False)
        self.assertEqual(CorporatePassword("abbceffg"), False)
        self.assertEqual(CorporatePassword("abbcegjk"), False)
        self.assertEqual(CorporatePassword("abcdefgh"), False)
        self.assertEqual(CorporatePassword("ghijklmn"), False)
        self.assertEqual(CorporatePassword("abcdffaa"), True)
        self.assertEqual(CorporatePassword("ghjaabcc"), True)
