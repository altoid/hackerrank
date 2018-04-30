#!/usr/bin/env python

from pprint import pprint, pformat

def coin_change(amount, coins):
    """
    returns the answer and the total number of recursive calls
    to coin_change.
    """

    if not coins:
        return 0, 1

    if amount == 0:
        return 1, 1

    if amount < 0:
        return 0, 1

    total1, count1 = coin_change(amount, coins[:-1])
    total2, count2 = coin_change(amount - coins[-1], coins)

    return total1 + total2, count1 + count2


def solve(amount, coins):
    pprint("amount = %s" % amount)
    pprint("coins = %s" % coins)
    result = coin_change(amount, coins)
    print "solution:  %s" % result[0]
    print "total calls to coin_change:  %s" % result[1]


if __name__ == '__main__':

    # dictionary which will map (amount, ncoins) tuples to solution
    # for that combination

    prior_solutions = {}

    solve(4, [1,2,3])  # 4, 13
    solve(10, [2,3,5,6]) # 5, 33
    solve(10, [2,3,5,6,19]) # 5, 34
    solve(100, [1, 5, 10, 25]) # 242, 6964

#    solve(250, [41, 34, 46, 9, 37, 32, 42, 21, 7, 13, 1, 24,
#                3, 43, 2, 23, 8, 45, 19, 30, 29, 18, 35, 11])
#    15685693751
