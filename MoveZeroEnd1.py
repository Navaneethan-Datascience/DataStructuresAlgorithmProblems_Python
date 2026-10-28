'''
Accessing the all list elements using index values; if the element is '0' pop() the element append that into the default list
'''

def MoveZeroEnd(numbers) -> list:

    for num in range(len(numbers)):

        if numbers[num] == 0:
            zero = numbers.pop(num)
            numbers.append(zero)

    return numbers

print(MoveZeroEnd([0, 1, 0, 3, 12]))