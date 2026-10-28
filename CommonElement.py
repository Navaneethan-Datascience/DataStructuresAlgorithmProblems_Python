def CommonElement(numbers1, numbers2) -> list:

    cmn_element = []

    for num in numbers1:
        if num in numbers2:
            cmn_element.append(num)

    return cmn_element

print(CommonElement([1, 2, 3, 4],[3, 4, 5, 6]))
