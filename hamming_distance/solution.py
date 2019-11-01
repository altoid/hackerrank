#!/usr/bin/env python

import unittest
import fileinput

"""
convert character string to bit vector

# of bits in a number

"""

string_2_nibble = {
    'a': 0,
    'b': 1,

    'aa': 0,
    'ab': 1,
    'ba': 2,
    'bb': 3,

    'aaa': 0,
    'aab': 1,
    'aba': 2,
    'abb': 3,
    'baa': 4,
    'bab': 5,
    'bba': 6,
    'bbb': 7,

    'aaaa': 0,
    'aaab': 1,
    'aaba': 2,
    'aabb': 3,
    'abaa': 4,
    'abab': 5,
    'abba': 6,
    'abbb': 7,
    'baaa': 8,
    'baab': 9,
    'baba': 10,
    'babb': 11,
    'bbaa': 12,
    'bbab': 13,
    'bbba': 14,
    'bbbb': 15,
}


def countbits(n):
    """
    :param n: unsigned number
    :return: number of bits set in n
    """
    if n == 0:
        return 0

    c = 1
    while n & (n - 1):
        c += 1
        n = n & (n - 1)
    return c


def string_to_int(s):
    result = 0
    prefix_length = len(s) % 4
    if prefix_length:
        prefix = s[:prefix_length]
        result = string_2_nibble[prefix]
    ptr = prefix_length
    while ptr < len(s):
        snippet = s[ptr:(ptr + 4)]
        result = result * 16 + string_2_nibble[snippet]
        ptr += 4
    return result


def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("strings not same length")

    n1 = string_to_int(s1)
    n2 = string_to_int(s2)
    return countbits(n1 ^ n2)


def lyse(s, l, r):
    """
    split the string into 3 parts:
    1. left - the part to the left of the middle
    2. middle - the chars from l to r inclusive
    3. right - the part to the right of the middle

    left and right may be empty.  the middle never will be.

    :param s:
    :param l:
    :param r:
    :return:
    """

    left = s[:(l - 1)]
    middle = s[(l - 1):r]
    right = s[r:]

    return left, middle, right


def change(s, l, r, c):
    """
    in string s, change characters l through r into c.
    indexing is 1-based.

    string will never be ''
    """

    first, _, right = lyse(s, l, r)
    middle = c * (r - l + 1)
    return first + middle + right


def reverse(s, l, r):
    first, middle, right = lyse(s, l, r)
    return first + middle[::-1] + right


def swap(s, l1, r1, l2, r2):
    left_prefix, left_part, _ = lyse(s, l1, r1)
    _, right_part, right_suffix = lyse(s, l2, r2)
    middle = s[r1:(l2 - 1)]
    return left_prefix + right_part + middle + left_part + right_suffix

if __name__ == '__main__':
    fi = fileinput.FileInput()

    # throw away first line
    fi.readline()

    s = fi.readline().strip()

    # throw away next line
    fi.readline()

    # now read the commands
    cmdline = fi.readline().strip()
    while cmdline:
        args = cmdline.split()
        cmd = args[0]
        rest = args[1:]

        if cmd == 'C':
            l = int(rest[0])
            r = int(rest[1])
            c = rest[2]
            s = change(s, l, r, c)

        if cmd == 'S':
            l1 = int(rest[0])
            r1 = int(rest[1])
            l2 = int(rest[2])
            r2 = int(rest[3])
            s = swap(s, l1, r1, l2, r2)

        if cmd == 'R':
            l = int(rest[0])
            r = int(rest[1])
            s = reverse(s, l, r)

        if cmd == 'W':
            l = int(rest[0])
            r = int(rest[1])
            _, middle, _ = lyse(s, l, r)
            print middle

        if cmd == 'H':
            l1 = int(rest[0])
            l2 = int(rest[1])
            length = int(rest[2])

            _, part1, _ = lyse(s, l1, l1 + length - 1)
            _, part2, _ = lyse(s, l2, l2 + length - 1)
            d = hamming_distance(part1, part2)
            print d

        cmdline = fi.readline().strip()


class MyTest(unittest.TestCase):

    def test_swap(self):
        self.assertEqual('abcdLEFTxRIGHTdcba', swap('abcdRIGHTxLEFTdcba', 5, 9, 11, 14))
        self.assertEqual('LEFTRIGHT', swap('RIGHTLEFT', 1, 5, 6, 9))
        self.assertEqual('ab', swap('ba', 1, 1, 2, 2))

    def test_reverse(self):
        s = 'abcdLLATIKCUFefgh'
        self.assertEqual('abcdFUCKITALLefgh', reverse(s, 5, 13))

        s = 'LLATIKCUF'
        self.assertEqual('FUCKITALL', reverse(s, 1, 9))

    def test_lyse(self):
        s = 'CHEESE'
        first, middle, right = lyse(s, 1, 6)
        self.assertEqual('', first)
        self.assertEqual('CHEESE', middle)
        self.assertEqual('', right)

        first, middle, right = lyse(s, 3, 4)
        self.assertEqual('CH', first)
        self.assertEqual('EE', middle)
        self.assertEqual('SE', right)

    def test_change(self):
        self.assertEqual('aaaabbbbaaaa', change('aaaaaaaaaaaa', 5, 8, 'b'))

        self.assertEqual('b', change('a', 1, 1, 'b'))
        self.assertEqual('baaaa', change('aaaaa', 1, 1, 'b'))
        self.assertEqual('aabaa', change('aaaaa', 3, 3, 'b'))
        self.assertEqual('bbbbb', change('aaaaa', 1, 5, 'b'))

    def test_countbits(self):
        self.assertEqual(0, countbits(0))
        self.assertEqual(1, countbits(1))
        self.assertEqual(1, countbits(2))
        self.assertEqual(1, countbits(4))
        self.assertEqual(1, countbits(8))
        self.assertEqual(1, countbits(16))
        self.assertEqual(1, countbits(2 ** 5))
        self.assertEqual(1, countbits(2 ** 9))
        self.assertEqual(1, countbits(2 ** 111))

        self.assertEqual(2, countbits(2 ** 5 + 1))
        self.assertEqual(2, countbits(2 ** 9 + 2))
        self.assertEqual(2, countbits(2 ** 111 + 4))

        self.assertEqual(5, countbits(2 ** 5 - 1))
        self.assertEqual(9, countbits(2 ** 9 - 1))
        self.assertEqual(111, countbits(2 ** 111 - 1))

        self.assertEqual(3, countbits(2 ** 111 + 2 ** 9 + 2 ** 5))

    def test_string_to_int(self):
        self.assertEqual(0, string_to_int(''))

        self.assertEqual(0, string_to_int('a'))
        self.assertEqual(0, string_to_int('aa'))
        self.assertEqual(0, string_to_int('aaa'))
        self.assertEqual(0, string_to_int('aaaa'))
        self.assertEqual(0, string_to_int('aaaaa'))
        self.assertEqual(0, string_to_int('aaaaaa'))
        self.assertEqual(0, string_to_int('aaaaaaa'))
        self.assertEqual(0, string_to_int('aaaaaaaa'))

        self.assertEqual(1, string_to_int('b'))
        self.assertEqual(2, string_to_int('ba'))
        self.assertEqual(4, string_to_int('baa'))
        self.assertEqual(8, string_to_int('baaa'))
        self.assertEqual(16, string_to_int('baaaa'))
        self.assertEqual(32, string_to_int('baaaaa'))
        self.assertEqual(64, string_to_int('baaaaaa'))
        self.assertEqual(128, string_to_int('baaaaaaa'))
        self.assertEqual(256, string_to_int('baaaaaaaa'))

    def test_hamming_distance(self):
        self.assertEqual(0, hamming_distance('ababababababa', 'ababababababa'))

        self.assertEqual(2, hamming_distance('abbbbb', 'babbbb'))
        self.assertEqual(1, hamming_distance('abbbbb', 'bbbbbb'))
        self.assertEqual(5, hamming_distance('aaaaa', 'bbbbb'))

