def MissingNumber(lst):

    for i in range(len(lst) - 1):

        if lst[i+1] - lst[i] != 1:
		
           missing_number = lst[i] + 1

           lst.insert(i+1,missing_number)

           return lst


list1 = [1,2,3,4,5,7]
print(MissingNumber(list1))