def MoveZeroEnd(array):

    '''
	Using the index value in a given array, inside the loop checks if there is any value '0' identified in the array, it stores the value in a variable 
	and removes that value, and then the stored value will be appended to the default array.
    '''
    for i in range(len(array)):

        if array[i] == 0:

            value = array[i]

            array.pop(i)
            array.append(value)

    return array


arr = [0,1,0,3,0,12,15,0,34,65,0]

print(MoveZeroEnd(arr))