#!/usr/bin/env python

import unittest
import fileinput

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class SLList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, v):
        n = Node(v)
        if self.tail:
            self.tail.next = n
        self.tail = n
        if not self.head:
            self.head = n

    def reverse(self):
        """
        reverses the list in place
        :return: bupkus
        """
        cur = self.head
        prev = nechst = None
        while cur:
            nechst = cur.next
            cur.next = prev

            prev = cur
            cur = nechst
        self.tail = self.head
        self.head = prev

    def display(self):
        arr = []
        p = self.head
        while p:
            arr.append(p.value)
            p = p.next
        print "<%s>" % " ".join(arr)


if __name__ == '__main__':
    fi = fileinput.FileInput()

    ncases = int(fi.readline().strip())

    while ncases:
        nelements = int(fi.readline().strip())
        ll = SLList()
        while nelements:
            e = fi.readline().strip()
            ll.insert(e)
            nelements -= 1

        ncases -= 1
        ll.display()
        ll.reverse()
        ll.display()