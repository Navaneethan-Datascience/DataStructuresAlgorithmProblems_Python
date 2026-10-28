def LongestIncreaseSequence(numbers) -> int:

    
    cur_streak = 1
    long_streak = 1
    
    for n in range(len(numbers)-1):

        if numbers[n+1] > numbers[n]:
            cur_streak += 1

        else:
            cur_streak = 1

        if cur_streak > long_streak:
            long_streak = cur_streak


    return long_streak

print(LongestIncreaseSequence([1, 2, 3, 1, 2, 3, 4, 0]))