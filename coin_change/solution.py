#!/usr/bin/env python

from pprint import pprint, pformat

def coin_change(amount, coins):
    """
    returns the answer and the total number of recursive calls
    to coin_change.
    """
    ncoins = len(coins)

    if (amount, ncoins) in prior_solutions:
        return prior_solutions[(amount, ncoins)], 0

    if not coins:
        return 0, 1

    if amount == 0:
        return 1, 1

    if amount < 0:
        return 0, 1

    total1, count1 = coin_change(amount, coins[:-1])
    total2, count2 = coin_change(amount - coins[-1], coins)

    # number of ways to give change without one denomination
    # + number of ways to give change for the amount minus one denomination
    # 
    # ex
    # solve(10, [2,3,5,6])
    # make change without a 6 + give me a 6 then make change for 4

    prior_solutions[(amount, ncoins)] = total1 + total2

    return total1 + total2, count1 + count2


def solve(amount, coins):
    global prior_solutions

    prior_solutions = {}

    print "amount = %s" % amount
    print "coins = %s" % coins
    result = coin_change(amount, coins)
    print "solution:  %s" % result[0]
    print "total calls to coin_change:  %s" % result[1]


if __name__ == '__main__':

    solve(4, [1,2,3])  # 4, 13/8
    solve(10, [2,3,5,6]) # 5, 33/16
    solve(10, [2,3,5,6,19]) # 5, 34/17
    solve(100, [1, 5, 10, 25]) # 242, 6964/105

    solve(250, [41, 34, 46, 9, 37, 32, 42, 21, 7, 13, 1, 24,
                3, 43, 2, 23, 8, 45, 19, 30, 29, 18, 35, 11])  #    15685693751

    solve(219, [36, 10, 42, 7, 50, 1, 49, 24, 37, 12, 34, 13,
                39, 18, 8, 29, 19, 43, 5, 44, 28, 23, 35, 26]) # 168312708

