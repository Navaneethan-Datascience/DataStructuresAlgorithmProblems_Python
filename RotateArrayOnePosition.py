def RotateArrayOnePosition(array):

    array.insert(0,array.pop()) #it removes the last element from the list, adds that element as the first element.

    return array

arr = [1,2,3,4]
print(RotateArrayOnePosition(arr))