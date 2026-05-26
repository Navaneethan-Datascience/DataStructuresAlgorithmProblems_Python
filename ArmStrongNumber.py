def ArmStrongNumber(num):

    original_num = num
    sum = 0

    #it checks whether the given number is an Armstrong number or notr not.
    while num > 0:

        last_digit = num % 10
        cube_value = last_digit ** 3

        sum = sum + cube_value

        num = num // 10

    if sum == original_num:

        print("The given number is Armstrong number: ", sum)

    else:

        print("The given number is not Armstrong number: ", sum)


number = int(input("Enter a number: "))

ArmStrongNumber(number)