
def MostFrequentPairConsecutiveValues(numbers):

    counts = {}

    for i in range(len(numbers) - 1):

        pair = (numbers[i], numbers[i + 1])

        if pair in counts:
            counts[pair] += 1
        else:
           counts[pair] = 1

    most_frequent = max(counts, key=counts.get)
    return most_frequent

print(MostFrequentPairConsecutiveValues([1, 2, 1, 2, 1, 2, 3]))