#!/usr/bin/env python

import fileinput

BOARDSIZE = 10

# assume no 1-letter words

# words are sorted by length, then alphabetically

if __name__ == '__main__':
    fi = fileinput.FileInput()
    board = []
    for _ in xrange(BOARDSIZE):
        board.append(fi.readline().strip())

    print board

    # read the words
    words = fi.readline().strip().split(';')
    print words

    # scan the board: across
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
                    currentrun = (row, col, 1)

            elif lastchar == '-':
                if c == '+':
                    if currentrun[2] > 1:
                        print "across run:  %s" % (currentrun,)
                    currentrun = None
                elif c == '-':
                    currentrun = (currentrun[0], currentrun[1], currentrun[2] + 1)

            elif lastchar == '+':
                if c == '+':
                    pass
                elif c == '-':
                    currentrun = (row, col, 1)

            lastchar = c
            
        if currentrun and currentrun[2] > 1:
            print "across run:  %s" % (currentrun,)
            
    # scan the board: down
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
                    currentrun = (row, col, 1)

            elif lastchar == '-':
                if c == '+':
                    if currentrun[2] > 1:
                        print "down run:  %s" % (currentrun,)
                    currentrun = None
                elif c == '-':
                    currentrun = (currentrun[0], currentrun[1], currentrun[2] + 1)

            elif lastchar == '+':
                if c == '+':
                    pass
                elif c == '-':
                    currentrun = (row, col, 1)

            lastchar = c
            
        if currentrun and currentrun[2] > 1:
            print "down run:  %s" % (currentrun,)
