def LongestStreak(lst1):

    current_length = 1
    max_length = 1

    for i in range(len(lst1) - 1):

        if lst1[i + 1] > lst1[i]:

            current_length += 1

        else:

            current_length = 1

        if current_length > max_length:

            max_length = current_length

    return max_length


list1 = [1,2,3,1,2,3,4,1]

print(LongestStreak(list1))