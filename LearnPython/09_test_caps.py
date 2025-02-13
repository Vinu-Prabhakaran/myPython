import unittest
from module_to_test import caps_text, title_text


class TestCaps(unittest.TestCase):
    def test_caps_with_one_word(self):
        result = caps_text('vinu')
        self.assertEqual(result, 'Vinu')

    def test_caps_with_multiple_words(self):
        result = caps_text('this world is beautiful')
        self.assertEqual(result, 'This world is beautiful')

    def test_title_with_multiple_words(self):
        result = title_text('this world is beautiful')
        self.assertEqual(result, 'This World Is Beautiful')


if __name__ == '__main__':
    unittest.main()
