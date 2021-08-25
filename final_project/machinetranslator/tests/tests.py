import unittest

from translator import english_to_french, french_to_english


class Test(unittest.TestCase):
    def test_text(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def null_import(self):
        self.assertIsNotNone(english_to_french(None), 'Bonjour')
        self.assertIsNotNone(french_to_english(None), 'Hello')


if __name__ == '__main__':
    unittest.main()
