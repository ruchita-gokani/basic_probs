import unittest
import basic_probs.is_leap_year as leap_year


class TestLeapYear(unittest.TestCase):
    def test_is_leap_year(self):
        result = leap_year.is_leap(2021)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
