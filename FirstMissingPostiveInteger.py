
'''
#Brootforce solution
def FirstMissingPostiveInteger(lst1):


    #checks whether the integer numbers are present in the list or not.
    for i in range(1,len(lst1)+2):

        if i not in lst1:

           return i

list1 = [1,2,3]
print(FirstMissingPostiveInteger(list1))

'''

#optimized solution
def FirstMissingPostiveInteger(lst1):


    #checks whether the integer numbers are present in the list or not.

    numbers = set(lst1)

    i = 1

    while i in lst1:

          i += 1

    return i

list1 = [1,2,3]
print(FirstMissingPostiveInteger(list1))
