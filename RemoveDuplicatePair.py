'''
1. Read each pair in the tuple.
2. Store the pair in a set()
3. those are the pair values are not in the set; it will be appended in the list
'''

def RemoveDuplicatePair(pairlist):

    distinct_pair = []
    seen = set()

    for pair in pairlist:

        if pair not in seen:
            
            distinct_pair.append(pair)
            seen.add(pair)

    return distinct_pair
        

print(RemoveDuplicatePair([(1, 2), (3, 4), (1, 2), (5, 6)]))
