def intersection(lst1,lst2):

    #returns the common element in list.
    return list(set(lst1) & set(lst2)) 


list1 = [1,2,3,4]
list2 = [3,4,5,6]
print(intersection(list1,list2))