
def MergeList(list1, list2):
    result = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            # Append the smaller element
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
        
    # Append any remaining elements from list1
    while i < len(list1):
        result.append(list1[i])
        i += 1

    # Append any remaining elements from list2
    while j < len(list2):
        result.append(list2[j])
        j += 1


    return result


print(MergeList([1, 4, 7], [2, 3, 8]))
# Expected: [1, 2, 3, 4, 7, 8]
