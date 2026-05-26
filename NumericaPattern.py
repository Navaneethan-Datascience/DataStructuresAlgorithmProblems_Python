def main():

    numbers = [2,4,7,11,22]

    difference = []

    # Find differences
    for i in range(len(numbers) - 1):

        difference.append(numbers[i+1] - numbers[i])

    # Find missing number
    for i in range(len(difference) - 1):

        expected_difference = difference[i] + 1

        if difference[i+1] != expected_difference:

            missing_number = numbers[i+1] + expected_difference

            print("Missing number:", missing_number)

            # Insert missing number in correct position
            numbers.insert(i+2, missing_number)

            print(numbers)

if __name__ == "__main__":
    main()


'''
understand the pattern for calculations

1. decompose the problem
2. Build a common formula that solves the problem like 'difference = list[1] - list[0]'
3. Make that formula  dynamic using loops
4. Define the perfect condition

''' 