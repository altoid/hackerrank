#!/usr/bin/env python

import fileinput
import permute

BOARDSIZE = 10
ACROSS = 0
DOWN = 1

# assume no 1-letter words

class Run(object):
    def __init__(self, r, c, length, dir):
        self.row = r
        self.col = c
        self.length = length
        self.dir = dir

    def __str__(self):
        return "[row %s, col %s, len %s, dir %s]" % (
            self.row, self.col, self.length, 'DOWN' if self.dir else 'ACROSS')

    def __repr__(self):
        return str(self)

# words are sorted by length, then alphabetically
def my_compare(a, b):
    if len(a) == len(b):
        return cmp(a, b)

    if len(a) < len(b):
        return -1

    return 1

def test_solution(soln):
    print soln

if __name__ == '__main__':
    fi = fileinput.FileInput()
    board = []
    for _ in xrange(BOARDSIZE):
        board.append(fi.readline().strip())

    print board

    # read the words
    words = map(lambda x: x.upper(), fi.readline().strip().split(';'))

    # scan the board: across
    across_runs = []
    for row in xrange(BOARDSIZE):
        # '' -> '-'
        # '' -> '+'
        # '-' -> '-'
        # '-' -> '+'
        # '+' -> '-'
        # '+' -> '+'
        
        lastchar = None
        currentrun = None
        for col in xrange(BOARDSIZE):
            c = board[row][col]
            if not lastchar:
                if c == '+':
                    pass
                elif c == '-':
                    currentrun = Run(row, col, 1, ACROSS)

            elif lastchar == '-':
                if c == '+':
                    if currentrun.length > 1:
                        across_runs.append(currentrun)
                    currentrun = None
                elif c == '-':
                    currentrun.length += 1

            elif lastchar == '+':
                if c == '+':
                    pass
                elif c == '-':
                    currentrun = Run(row, col, 1, ACROSS)

            lastchar = c
            
        if currentrun and currentrun.length > 1:
            across_runs.append(currentrun)
            
    # scan the board: down
    down_runs = []
    for col in xrange(BOARDSIZE):
        # '' -> '-'
        # '' -> '+'
        # '-' -> '-'
        # '-' -> '+'
        # '+' -> '-'
        # '+' -> '+'
        
        lastchar = None
        currentrun = None
        for row in xrange(BOARDSIZE):
            c = board[row][col]
            if not lastchar:
                if c == '+':
                    pass
                elif c == '-':
                    currentrun = Run(row, col, 1, DOWN)

            elif lastchar == '-':
                if c == '+':
                    if currentrun.length > 1:
                        down_runs.append(currentrun)
                    currentrun = None
                elif c == '-':
                    currentrun.length += 1

            elif lastchar == '+':
                if c == '+':
                    pass
                elif c == '-':
                    currentrun = Run(row, col, 1, DOWN)

            lastchar = c
            
        if currentrun and currentrun.length > 1:
            down_runs.append(currentrun)

    print "across_runs: %s" % across_runs
    print "down_runs: %s" % down_runs

    all_runs = across_runs + down_runs
    all_lengths = map(lambda x: x.length, all_runs)
    print "all_runs: %s" % all_runs
    print "all_lengths: %s" % all_lengths

    # sort the words, first by length, then lexicographically
    
    print words
    s = sorted(words, cmp=my_compare)
    print s
    print "#" * 44
    for x in permute.permute(s, my_compare):
        lens = map(len, x)
        if lens == all_lengths:
            test_solution(x)


