''''
1. each num from list subtracted from the target
2. checks the subtracted result in the list; if it is the num appended to the result array
'''


def SumTarget(numbers, target) -> list:

    target_pair = []

    for num in numbers:

        complement_num = target - num

        if complement_num in numbers:

            target_pair.append(complement_num)

    return target_pair

print(SumTarget([7, 11, 2, 15],26))
