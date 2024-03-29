#!/usr/bin/env python

import fileinput


def pairwise_differences(s):
    # return pairs of indices of differences in the palindrome candidate.
    # for 1110000222, return [(0, 9), (1, 8), (2, 7)]
    if not s:
        return []

    m = len(s) / 2
    r = len(s) - 1
    l = 0
    result = []
    for i in xrange(m):
        if s[l] != s[r]:
            result.append(tuple([l, r]))
        r -= 1
        l += 1
    return result


def highestValuePalindrome(s, n, k):
    # s - number
    # n - number of digits in number
    # k - max number of changes we can make.

    digits = list(s)
    diffs = pairwise_differences(digits)
    if k < len(diffs):
        return str(-1)

    # make several passes:
    # 1 - change one digit in each pair to be the largest of the digits in the pair
    # 2 - if we can keep going, change SAME digits to 9s
    # 3 - if we can keep going, and # of digits is odd, change middle digit to 9 if we can.

    # pass 1
    for d in diffs:
        m = max(digits[d[0]], digits[d[1]])
        digits[d[0]] = m
        digits[d[1]] = m
        k -= 1

    # pass 2
    # create bit vector telling us which pairs we can still change.
    # 1 means the pair was already matched
    # 0 means we changed it
    check = [1] * (len(digits) / 2)
    for d in diffs:
        check[d[0]] = 0
    for i in xrange(len(check)):
        if k == 0:
            break

        if digits[i] == '9':
            continue

        if check[i]:
            if k < 2:
                continue
            digits[i] = '9'
            digits[len(digits) - 1 - i] = '9'
            k -= 2
        else:
            digits[i] = '9'
            digits[len(digits) - 1 - i] = '9'
            k -= 1

    # pass 3
    if k > 0:
        if len(digits) % 2 == 1:
            m = len(digits) / 2
            if digits[m] != '9':
                digits[m] = '9'
                k -= 1

    return ''.join(digits)


if __name__ == '__main__':
    fi = fileinput.FileInput()
    n, k = map(int, fi.readline().strip().split(' '))
    s = fi.readline().strip()
    result = highestValuePalindrome(s, n, k)
    print result
