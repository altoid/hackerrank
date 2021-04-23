#!/usr/bin/env python


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def make_tree(l):
    if not l:
        return None

    root = None
    for n in l:
        newnode = Node(n)
        if not root:
            root = newnode
            continue

        ptr = root
        while True:
            if n < ptr.info:
                if ptr.left:
                    ptr = ptr.left
                    continue

                ptr.left = newnode
                break

            if n > ptr.info:
                if ptr.right:
                    ptr = ptr.right
                    continue

                ptr.right = newnode
                break
    return root


def path_to(root, a):
    # returns empty list if a not found

    ptr = root
    result = []
    while True:
        result.append(ptr.info)
        if ptr.info == a:
            return result

        if a < ptr.info:
            ptr = ptr.left
        else:
            ptr = ptr.right

        if not ptr:
            # not found
            return []


def lca(node, a, b):
    # find path from root to a
    # find path from root to b
    # the LCA is the furthest node in each path that is common to both
    # returns None if no LCA

    a_path = path_to(node, a)
    b_path = path_to(node, b)

    result = None
    i = 0
    while i < len(a_path) and i < len(b_path):
        if a_path[i] == b_path[i]:
            result = a_path[i]
        i += 1
    return result


def test(tree_arr, tests):
    root = make_tree(tree_arr)
    for t in tests:
        result = lca(root, t[0], t[1])
        print "LCA of %s is %s" % (t, result)


if __name__ == '__main__':
    test([4, 2, 7, 1, 3, 6], [(1, 3), (11, 22), (11, 4), (6, 6), (1, 7)])
