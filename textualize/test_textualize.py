import unittest

from textualize import textualize

class Test_textualize(unittest.TestCase):

    def test_single_digits(self):
        test_items = [
                (0, 'zero'),
                (1, 'one'),
                (2, 'two'),
                (3, 'three'),
                (4, 'four'),
                (5, 'five'),
                (6, 'six'),
                (7, 'seven'),
                (8, 'eight'),
                (9, 'nine')
        ]
        for num, num_string in test_items:
            self.assertEqual(num_string, textualize(num))

    def test_two_digits_less_than_twenty(self):
        test_items = [
                (10, 'ten'),
                (11, 'eleven'),
                (12, 'twelve'),
                (13, 'thirteen'),
                (14, 'fourteen'),
                (15, 'fifteen'),
                (16, 'sixteen'),
                (17, 'seventeen'),
                (18, 'eighteen'),
                (19, 'nineteen')
        ]
        for num, num_string in test_items:
            self.assertEqual(num_string, textualize(num))

    def test_powers_of_ten(self):
        test_items = [
                (1, 'one'),
                (10, 'ten'),
                (100, 'one hundred'),
                (1000, 'one thousand'),
                (10000, 'ten thousand'),
                (100000, 'one hundred thousand'),
                (1000000, 'one million'),
                (10000000, 'ten million'),
                (100000000, 'one hundred million'),
                (1000000000, 'one billion'),
                (10000000000, 'ten billion'),
                (100000000000, 'one hundred billion'),
                (1000000000000, 'one trillion'),
                (10000000000000, 'ten trillion'),
                (100000000000000, 'one hundred trillion'),
                (1000000000000000, 'one quadrillion'),
                (10000000000000000, 'ten quadrillion'),
                (100000000000000000, 'one hundred quadrillion'),
                (1000000000000000000, 'one quintillion')
        ]
        for num, num_string in test_items:
            self.assertEqual(num_string, textualize(num))

    def test_powers_of_two(self):
        test_items = [
                (2, 'two'),
                (4, 'four'),
                (8, 'eight'),
                (16, 'sixteen'),
                (32, 'thirty-two'),
                (64, 'sixty-four'),
                (128, 'one hundred twenty-eight'),
                (256, 'two hundred fifty-six'),
                (512, 'five hundred twelve'),
                (1024, 'one thousand twenty-four'),
                (2048, 'two thousand forty-eight'),
                (4096, 'four thousand ninety-six'),
                (8192, 'eight thousand one hundred ninety-two')
        ]
        for num, num_string in test_items:
            self.assertEqual(num_string, textualize(num))

    def test_negative_numbers(self):
        test_items = [
                (-1, 'negative one'),
                (-18, 'negative eighteen'),
                (-250, 'negative two hundred fifty'),
                (-5000, 'negative five thousand')
        ]

    def test_arbitrary_numbers(self):
        # arbitrarily chosen
        test_items = [
                (30, 'thirty'),
                (42, 'forty-two'),
                (255, 'two hundred fifty-five'),
                (404, 'four hundred four'),
                (1337, 'one thousand three hundred thirty-seven'),
                (200000, 'two hundred thousand'),
                (1000001, 'one million one')
        ]
        for num, num_string in test_items:
            self.assertEqual(num_string, textualize(num))
