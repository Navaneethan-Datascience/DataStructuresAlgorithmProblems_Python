
'''
input num not in seen set; update the list and set
the end output keeps the same order of the element but with unique values
'''

def RemoveDuplicate(numbers) -> list:

    result = []
    seen = set()

    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result

print(RemoveDuplicate([3, 1, 3, 2, 1, 4]))