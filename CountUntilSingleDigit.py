def main():

    number = int(input('Enter a number: '))

    total = 0

    # Step 1: sum digits
    while number > 0:

        last_digit = number % 10
        total = total + last_digit

        number = number // 10

    # Step 2: reduce to single digit
    while total >= 10:

        temp = 0

        while total > 0:

            last_num = total % 10
            temp = temp + last_num

            total = total // 10

        total = temp

    print('Single digit summation value of the given number:', total)

if __name__ == "__main__":
    main()