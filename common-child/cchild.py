#!/usr/bin/env python

# https://www.hackerrank.com/challenges/common-child/problem

# in this case the two input strings are the same length, which is a special case
# of the LCS problem.  but this solution can (nay, must) handle strings of different lengths

import pprint

pp = pprint.PrettyPrinter()


def lcs(string1, string2):
    if len(string1) == 0 or len(string2) == 0:
        return 0

    if string1[0] == string2[0]:
        return 1 + lcs(string1[1:], string2[1:])

    return max(lcs(string1, string2[1:]), lcs(string1[1:], string2))


def lcs_matrix(string1, string2):
#    if len(string1) != len(string2):
#        raise Exception("strings must be the same length")

    if len(string1) == 0:
        return 0

    # ref:  https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
    # we can do this without allocating a giant matrix.  instead, need just
    # two rows.

    list1 = [0] * (len(string2) + 1)
    list2 = [0] * (len(string2) + 1)

    # pp.pprint(list1)
    for c1 in string1:
        j = 1
        for c2 in string2:
            if c1 == c2:
                list2[j] = list1[j - 1] + 1
            else:
                list2[j] = max(list2[j - 1], list1[j])
            j += 1

        # pp.pprint(list2)
        list1 = list2
        list2 = [0] * (len(string2) + 1)

    return list1[-1]
