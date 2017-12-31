#!/usr/bin/env python

# https://www.hackerrank.com/challenges/common-child/problem

import pprint

pp = pprint.PrettyPrinter()

# map each letter in the first string to a list of its indices in the string.
# 
# for each letter in the second string,
# look it up in the hash table.

def build_hash(s):
    hash = {}
    for e in enumerate(s):
        idx, key = e
        if not hash.get(key):
            hash[key] = []
        hash[key].append(idx)

    return hash
        
#strings = ['ASTRINGXISSAIDTOBEACHILDOFASTRINGYIFXCANBEFORMEDBYDELETINGZEROORMORECHARACTERSFROMY',
#           'HATYOUGETTHEGISTOFITTHERESTOFITSPECIFIESTHE']

def helper(chars, hash):
    tuples = [(chars[0], x) for x in hash[chars[0]]]
#    print tuples
    if len(chars) == 1:
        l = [[t] for t in tuples]
#        print l
        return l

    # stick each tuple in to each list returned by the recursive call
    prior = helper(chars[1:], hash)
#    print prior

    result = []
    for t in tuples:
        for p in prior:
            cp = list(p)
            cp.append(t)
            result.append(cp)
#    print result
    return result

def gen(chars, dict):
    result = helper(chars, dict)
    result = [sorted(r, cmp=lambda x, y: cmp(x[1], y[1])) for r in result]
#    print result
    return result

# H [1, 5] [2]
# A [6]    [3, 5, 6, 7]
# N [3, 7] [0]
