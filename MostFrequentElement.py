def MostFrequentElement(nums):

    element_frequence = {}

    for num in nums:

        element_frequence[num] = element_frequence.get(num,0)+1

    return max(element_frequence,key = element_frequence.get)

list1 = [1, 2, 3, 2, 4, 2, 5]
print(MostFrequentElement(list1))