#!/usr/bin/env python

import unittest
import fileinput


class Editor(object):
    APPEND = 1
    DELETE = 2
    PRINT = 3
    UNDO = 4

    def __init__(self):
        self.__text = ''
        self.__operations = []

    def append(self, w):
        self.__text += w
        record = (self.APPEND, w)
        self.__operations.append(record)

    def delete(self, k):
        amputation = self.__text[-k:]
        remainder = len(self.__text) - k
        self.__text = self.__text[:remainder]
        record = (self.DELETE, amputation)
        self.__operations.append(record)

    def printk(self, k):
        # print kth character (one-based)
        print self.__text[k - 1]

    def undo(self):
        if not self.__operations:
            return

        op = self.__operations.pop()
        if op[0] == self.APPEND:
            remainder = len(self.__text) - len(op[1])
            self.__text = self.__text[:remainder]

        elif op[0] == self.DELETE:
            self.__text += op[1]

    @property
    def text(self):
        return self.__text


if __name__ == '__main__':
    fi = fileinput.FileInput()
    ed = Editor()

    for line in fi:
        if fi.isfirstline():
            continue

        edit = line.strip().split(' ')
        operation = int(edit[0])
        if operation == ed.APPEND:
            ed.append(edit[1])
        elif operation == ed.DELETE:
            k = int(edit[1])
            ed.delete(k)
        elif operation == ed.PRINT:
            k = int(edit[1])
            ed.printk(k)
        elif operation == ed.UNDO:
            ed.undo()


class MyTest(unittest.TestCase):
    def test1(self):
        ed = Editor()
        ed.append('Simple')
        ed.append('Text')
        ed.append('Editor')
        ed.undo()
        self.assertEqual('SimpleText', ed.text)

    def test2(self):
        ed = Editor()
        ed.append('Simple')
        ed.append('Text')
        ed.delete(2)
        ed.append('rse')
        ed.append('Editor')

        self.assertEqual('SimpleTerseEditor', ed.text)

