def main():

    array = [1,3,2,5,7] #full array
    target = 10  #target value

    for i in range(0, len(array)-2):

	"""
	It assigns the i values as indices in the array and extracts the value in order, then sums the three values and stores them in 'value'.
	If it matches the target value, it gives true and prints the subarray.
	"""
        value = array[i] + array[i+1] + array[i+2]

        sub_array = array[i:i+3]

        if value == target:
            print('True')
            print(sub_array)

if __name__ == '__main__':
    main()