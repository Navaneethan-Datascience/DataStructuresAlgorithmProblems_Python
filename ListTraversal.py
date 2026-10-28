
'''
'n' instances of the elements; how many instances the loop wants to shifts elements from last to first
'''
def ListTraversal(numbers, n) -> list:

    if not numbers:
        return numbers

    for _ in range(n):
        pop1 = numbers.pop()
        numbers.insert(0,pop1)
    return numbers

print(ListTraversal([1, 2, 3, 3, 5], 3))