#!/usr/bin/env python

import unittest
from pprint import pprint

def whatFlavors(cost_arr, money):

    # create a map of ice creams to their index positions.
    i = 1
    cost_to_idx = {}
    for c in cost_arr:
        if not c in cost_to_idx:
            cost_to_idx[c] = []
        cost_to_idx[c].append(i)
        i += 1

    pprint(cost_to_idx)

    complements = {}
    for c in cost_arr:
        if c not in complements:
            if 0 < (money - c) < money:
                complements[c] = money - c

    pprint(complements)

    # traverse the complements dict.  if k = v and k doesn't map to two elements
    # in cost_to_idx, it's not the answer.
    
    for k, v in complements.items():
        if k == v and len(cost_to_idx[k]) == 2:
            result = sorted(cost_to_idx[k])
            break

        result = sorted([cost_to_idx[k][0], cost_to_idx[v][0]])
        break

    print result[0], result[1]

class MyTest(unittest.TestCase):
    
    def test1(self):
        money = 4
        costs = [1,4,5,3,2]
        whatFlavors(costs, money)
