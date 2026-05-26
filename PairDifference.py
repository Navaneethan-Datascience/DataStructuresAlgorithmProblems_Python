"""
def PairDifference(array, target):

    '''
    The loop value goes as an index in the array based on the index array value next value subtracted from first value it 
    executes if it matches the target value it prints "True" otherwise it prints "False".
    '''

    for i in range(len(array)):

        for j in range(i+1, len(array)):

            difference = abs(array[i] - array[j])

            if difference == target:
                print(array[i], ",", array[j])
                print("True")
                print(" ")

            else:

                print(array[i], ",", array[j])
                print("False")


arr = [1,5,3,4,2]
targ = 2

PairDifference(arr, targ)

"""


def PairDifference(array, target):

    for i in range(len(array)):

        difference = array[i] + target

        if difference in array:
            print("True")
            print(f"({difference}-{array[i]})")


arr = [1,5,3,4,2]
targ = 2

PairDifference(arr, targ)