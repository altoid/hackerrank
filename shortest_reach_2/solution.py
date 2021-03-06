#!/usr/bin/env python

import fileinput
from memory_profiler import profile
from pprint import pprint, pformat

class GraphException(Exception):
    pass


class DGraph(object):
    '''
    directed graph.
    '''
    # implemented as a dictionary that maps nodes to lists of
    # nodes.

    def __init__(self):
        self.adj_list = {}

        # dictionary mapping pairs of nodes to costs.
        self.costs = {}

    def __nonzero__(self):
        # returns true if the graph has > 0 nodes
        return len(self.adj_list) > 0

    def __len__(self):
        # returns the number of nodes in the graph.
        return len(self.adj_list)

    def addnode(self, n):
        if n in self.adj_list:
            raise GraphException("node %s is already in the graph" % n)
        self.adj_list[n] = []

    def addnodes(self, *nodes):
        for n in nodes:
            self.addnode(n)

    def contains(self, n):
        return n in self.adj_list

    def addedge(self, a, b, cost=1):
        '''
        add an edge from a to be with default cost 1
        '''
        if a not in self.adj_list:
            raise GraphException("origin %s not in graph" % a)

        if b not in self.adj_list:
            raise GraphException("terminus %s not in graph" % b)

        self.adj_list[a].append(b)
        self.costs[(a, b)] = cost

    def dump(self):
        pprint(self.adj_list)

    '''
    return the nodes in the graph, as a list
    '''
    def nodes(self):
        for k in self.adj_list.keys():
            yield k

    def edgecost(self, a, b):
        return self.costs[(a, b)]

    @profile
    def edges(self):
        for n in self.nodes():
            for arc in self.adj_list[n]:
                yield (n, arc, self.edgecost(n, arc))

    @profile
    def dijkstra(self, n):
        # single-source shortest pair problem
        if n not in self.adj_list:
            raise GraphException("node %s not in graph" % n)

        diff = {k for k in self.adj_list.keys()} - set([n])

        # construct dict mapping (origin, terminus) to cost
        bigc = {}

        # hack this to make it work with undirected graphs.  since the cost from node a to b is the same as from b to
        # a, just store one edge in bigc.  we will store the edge where origin < terminus according to node label.

        def setcost(e):
            t = (min(e[0], e[1]), max(e[0], e[1]))
            bigc[t] = e[2]

        def getcost(n1, n2):
            t = (min(n1, n2), max(n1, n2))
            return bigc.get(t)

        def contains(n1, n2):
            t = (min(n1, n2), max(n1, n2))
            return t in bigc

        for e in self.edges():
            setcost(e)

        #print "bigc:  %s" % pformat(bigc)
        bigd = {x: -1 for x in diff}
        for x in self.adj_list[n]:
            if contains(n, x):
                bigd[x] = getcost(n, x)

        while diff:
            # find the node in diff where v (cost) is minimum

            x = filter(lambda x: bigd[x] != -1, diff)
            x = [(i, bigd[i]) for i in x]
            if not x:
                break

            #print pformat(x)
            w, mincost = min(x, key=lambda x: x[1])
            #print w, mincost
            diff.remove(w)

            for v in diff:
                if not contains(w, v):
                    continue

                if bigd[v] == -1:
                    bigd[v] = bigd[w] + getcost(w, v)
                    continue

                bigd[v] = min(bigd[v], bigd[w] + getcost(w, v))

        return bigd


class UGraph(DGraph):
    '''
    implements an undirected graph.
    '''

    def __init__(self):
        super(UGraph, self).__init__()

    def addedge(self, a, b, cost=1):
        super(UGraph, self).addedge(a, b, cost)
        super(UGraph, self).addedge(b, a, cost)
        minnode, maxnode = min(a, b), max(a, b)
        self.costs[(minnode, maxnode)] = cost

    def edgecost(self, a, b):
        return self.costs[(min(a, b), max(a, b))]

    @profile
    def edges(self):
        # since this is an undirected graph, we have to be careful
        # about not putting back-and-forth edges into the result set.
        # we'll put edges in where the origin is lexicographically
        # less than the terminus

        for n in self.nodes():
            for arc in self.adj_list[n]:
                a1 = n
                a2 = arc
                if a1 < a2:
                    yield (a1, a2, self.edgecost(a1, a2))


#################################################
@profile
def shortestReach(nnodes, edges, start):
    # print nnodes
    # print pformat(edges)
    # print start

    # there might be multiple edges between two nodes.  throw out all but the min cost edge.
    d = {}
    for e in edges:
        t = (min(e[0], e[1]), max(e[0], e[1]))
        if t not in d or e[2] < d[t]:
            d[t] = e[2]
#    pprint(d)

    # construct the graph
    # nodes are numbered from 1
    gr = UGraph()
    for a in xrange(nnodes):
        # node numbering is 1-based
        gr.addnode(a + 1)
    for k, v in d.items():
        gr.addedge(k[0], k[1], v)
    
    #gr.dump()

    result = gr.dijkstra(start)

    #print "d: %s" % pformat(result)
    return map(lambda x: result[x], sorted(result.keys()))


if __name__ == '__main__':
    fi = fileinput.FileInput()
    ncases = int(fi.readline().strip())
    for _ in xrange(ncases):
        nnodes, nedges = map(int, fi.readline().strip().split(' '))
        edges = []
        for _ in xrange(nedges):
            edges.append(map(int, fi.readline().strip().split(' ')))
        start = int(fi.readline().strip())

        result = shortestReach(nnodes, edges, start)
        print ' '.join(map(str, result))



