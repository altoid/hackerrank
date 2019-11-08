#!/usr/bin/env python

import unittest

import fileinput


def categorize(arr):

    # maps each word to a 2-item list:  [first line, # occurrences]
    d = {}
    line_no = 1

    for w in arr:
        if w not in d:
            d[w] = [line_no, 0]
        d[w][1] += 1

        line_no += 1

    return d


def nwords(d):
    return len(d)


def word_order(d):
    values = [x for x in d.values()]
    values = sorted(values, key=lambda x: x[0])
    values = [x[1] for x in values]
    return values


if __name__ == '__main__':
    fi = fileinput.FileInput()
    arr = []

    # throw away first line
    fi.readline()

    word = fi.readline()
    while word:
        word = word.strip()
        arr.append(word)
        word = fi.readline()

    d = categorize(arr)

    # print # of distinct words
    print nwords(d)

    print ' '.join(map(str, word_order(d)))


