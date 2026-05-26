def SecondLargest(array):

    sorted_array = sorted(array)

    return sorted_array[-2]

arr = [4,8,2,10,6]
print(SecondLargest(arr))