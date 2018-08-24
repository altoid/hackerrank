import unittest
import solution


class Tests(unittest.TestCase):
    def test_pairwise_differences(self):
        d = solution.pairwise_differences('')
        self.assertEqual(0, len(d))

        d = solution.pairwise_differences(list('123454321'))
        self.assertEqual(0, len(d))

        d = solution.pairwise_differences('12344321')
        self.assertEqual(0, len(d))

        d = solution.pairwise_differences('12345678')
        self.assertEqual([(0, 7), (1, 6), (2, 5), (3, 4)], d)

        d = solution.pairwise_differences('123456789')
        self.assertEqual([(0, 8), (1, 7), (2, 6), (3, 5)], d)

    def test_hvp_exact(self):
        s = '3943'
        r = solution.highestValuePalindrome(s, 0, 1)
        self.assertEqual('3993', r)

        s = '3843'
        r = solution.highestValuePalindrome(s, 0, 1)
        self.assertEqual('3883', r)

        s = '3483'
        r = solution.highestValuePalindrome(s, 0, 1)
        self.assertEqual('3883', r)

        # in this case there are 2 pairs of diffs, one is a 9
        s = '092282'
        r = solution.highestValuePalindrome(s, 0, 3)
        self.assertEqual('992299', r)

        s = '092282'
        r = solution.highestValuePalindrome(s, 0, 2)
        self.assertEqual('292292', r)

    def test_hvp_k_too_small(self):
        s = '0011'
        r = solution.highestValuePalindrome(s, 0, 1)
        self.assertEqual(-1, r)

    def test_hvp_increase_k_odd(self):
        s = '11100400222'
        r = solution.highestValuePalindrome(s, 0, 3)
        self.assertEqual('22200400222', r)

        s = '11100400222'
        r = solution.highestValuePalindrome(s, 0, 4)
        self.assertEqual('92200400229', r)

        s = '11100400222'
        r = solution.highestValuePalindrome(s, 0, 5)
        self.assertEqual('99200400299', r)

        s = '11100400222'
        r = solution.highestValuePalindrome(s, 0, 6)
        self.assertEqual('99900400999', r)

        s = '11100400222'
        r = solution.highestValuePalindrome(s, 0, 7)
        self.assertEqual('99900900999', r)

        s = '11100400222'
        r = solution.highestValuePalindrome(s, 0, 8)
        self.assertEqual('99990409999', r)

        s = '11100400222'
        r = solution.highestValuePalindrome(s, 0, 9)
        self.assertEqual('99990909999', r)

        s = '11100400222'
        r = solution.highestValuePalindrome(s, 0, 10)
        self.assertEqual('99999499999', r)

        s = '11100400222'
        r = solution.highestValuePalindrome(s, 0, 11)
        self.assertEqual('99999999999', r)

        s = '11100400222'
        r = solution.highestValuePalindrome(s, 0, 100)
        self.assertEqual('99999999999', r)

    def test_hvp_increase_k_even(self):
        s = '1110000222'
        r = solution.highestValuePalindrome(s, 0, 3)
        self.assertEqual('2220000222', r)

        s = '1110000222'
        r = solution.highestValuePalindrome(s, 0, 4)
        self.assertEqual('9220000229', r)

        s = '1110000222'
        r = solution.highestValuePalindrome(s, 0, 5)
        self.assertEqual('9920000299', r)

        s = '1110000222'
        r = solution.highestValuePalindrome(s, 0, 6)
        self.assertEqual('9990000999', r)

        s = '1110000222'
        r = solution.highestValuePalindrome(s, 0, 7)
        self.assertEqual('9990000999', r)

        s = '1110000222'
        r = solution.highestValuePalindrome(s, 0, 8)
        self.assertEqual('9999009999', r)

        s = '1110000222'
        r = solution.highestValuePalindrome(s, 0, 9)
        self.assertEqual('9999009999', r)

        s = '1110000222'
        r = solution.highestValuePalindrome(s, 0, 10)
        self.assertEqual('9999999999', r)

        s = '1110000222'
        r = solution.highestValuePalindrome(s, 0, 100)
        self.assertEqual('9999999999', r)

    def test_pass1(self):
        s = '12345678'
        r = solution.highestValuePalindrome(s, 0, 3)
        self.assertEqual(-1, r)

        s = '12345678'
        r = solution.highestValuePalindrome(s, 0, 4)
        self.assertEqual('87655678', r)

        s = '123405678'
        r = solution.highestValuePalindrome(s, 0, 4)
        self.assertEqual('876505678', r)

        s = '1002003004005006007008'
        r = solution.highestValuePalindrome(s, 0, 4)
        self.assertEqual('8007006005005006007008', r)

        s = '10020030040905006007008'
        r = solution.highestValuePalindrome(s, 0, 4)
        self.assertEqual('80070060050905006007008', r)


if __name__ == '__main__':
    unittest.main()
