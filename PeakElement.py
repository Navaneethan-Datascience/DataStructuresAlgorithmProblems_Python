def PeakElement(array):


    for i in range(1,len(array)-1):

	#checks the condition if the left and right sides of the value are greater or not.
        if array[i] > array[i+1] and array[i] > array[i-1]: 

           return array[i]


arr = [1,3,20,4,1]
print(PeakElement(arr))