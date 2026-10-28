'''
This is single pass method usebud here to indentify the second largest number of the array/lis
there some other methods, those are
    1. sort and filter
    2. heapq
but the current approach is have less time and storage complexity.
'''

def SecondLargest(nums):

    #Not enough elements
    if len(nums) < 2:
        return None

    max1 = 0
    max2 = 0

    '''
    1. input num > maximum number; maximum number = input num
    2. second maximum =  maximum number
    3. maximum num > input num > second maximum; then second maximum = input num
    '''
    for n in nums:

        if n > max1:
            max1, max2 = n, max1
        elif max1 > n > max2:
            max2 = n

    return max2

print(SecondLargest([4, 8, 2, 10, 8, 6]))
