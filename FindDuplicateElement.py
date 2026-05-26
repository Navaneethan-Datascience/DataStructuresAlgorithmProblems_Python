def FindDuplicateElement(array):

    duplicates = [] 
    seen = set() #to store the seen value because the seen value doesn't allow duplicate values
    
    #checks if the value in 'seen' is already there, if it is, it stores the value in 'duplicates'; otherwise, it add the to the 'seen'
    for item in array:

        if item in seen:
            duplicates.append(item)

        else:
            seen.add(item)

    return duplicates, seen


numbers = [1,2,3,4,1,4,2,3,5,6,7]

print(FindDuplicateElement(numbers))