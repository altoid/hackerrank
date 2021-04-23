#!/usr/bin/env python

import fileinput


class Queue:
    def __init__(self):
        self.push_to = []
        self.pull_from = []

    def enqueue(self, value):
        self.push_to.append(value)

    def pull(self):
        if self.len() == 0:
            return None

        if not self.pull_from:
            self.invert()

        return self.pull_from.pop()

    def head(self):
        if self.len() == 0:
            return None

        if not self.pull_from:
            self.invert()

        return self.pull_from[-1]

    def invert(self):
        # put everything in push_to into pull_from and empty out push_to
        # only do this if pull_from is empty
        if self.pull_from:
            raise RuntimeError("pull_from is not empty")

        self.push_to.reverse()
        self.pull_from = self.push_to
        self.push_to = []

    def len(self):
        return len(self.pull_from) + len(self.push_to)


if __name__ == '__main__':
    q = Queue()

    fi = fileinput.FileInput()
    for line in fi:
        if fi.isfirstline():
            continue

        values = map(int, line.strip().split(' '))
        if values[0] == 1:
            q.enqueue(values[1])
        elif values[0] == 2:
            x = q.pull()
        elif values[0] == 3:
            print q.head()

