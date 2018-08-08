def next_permutation(mylist):
    # return the permutation that lexicographically follows
    # <mylist>, or None if there is no such permutation
    #
    # algorithm:
    # - scan RL to first item x that is smaller than
    #   the one to its right
    # - swap it with the smallest item to the right
    #   of x that is larger than x (y)
    # - sort the list [x+1:]

    l = len(mylist)
    if l < 2:
        return

    current = l - 2
    following = l - 1
    while current >= 0:
        if mylist[current] < mylist[following]:
            #print "ack - current = %s, following = %s, list = %s" % (current, following, mylist)
            # find the smallest item to the right of
            # mylist[current] that is bigger
            # than mylist[current]
            k = following
            m = mylist[k]
            mi = k
            while k < l:
                if mylist[current] < mylist[k] < m:
                    m = mylist[k]
                    mi = k
                k += 1

            mylist_copy = list(mylist)
            mylist_copy[current], mylist_copy[mi] = mylist_copy[mi], mylist_copy[current]
            return mylist_copy[:following] + sorted(mylist_copy[following:])
        
        current -= 1
        following -= 1
    
def prev_permutation(mylist):
    # return the permutation that lexicographically precedes
    # <mylist>, or None if there is no such permutation
    #
    # algorithm:
    # - scan RL to first item that is larger than
    #   the one to its right (x)
    # - swap it with the largest item to the right
    #   of x that is smaller than x (y)
    # - sort the list [x+1:] descending

    l = len(mylist)
    if l < 2:
        return

    c = l - 2
    current = c
    following = c + 1
    while current >= 0:
#        print "current = %d, following = %d" % (current, following)
        if mylist[current] > mylist[following]:
            # find the biggest item to the right of
            # mylist[current] that is smaller
            # than mylist[current]
            k = following
            m = mylist[k]
            mi = k
            while k < l:
                if m < mylist[k] < mylist[current]:
                    m = mylist[k]
                    mi = k
                k += 1

            mylist_copy = list(mylist)
            mylist_copy[current], mylist_copy[mi] = mylist_copy[mi], mylist_copy[current]
            return mylist_copy[:following] + sorted(mylist_copy[following:], reverse=True)
        
        current -= 1
        following -= 1
    
def permute(mylist):
    x = sorted(mylist)

    while x is not None:
        yield x
        x = next_permutation(x)

        
