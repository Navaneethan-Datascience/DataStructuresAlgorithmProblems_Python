def ProductDigits(number):

    #extracts the last digit of the number and multiplies it until the number becomes zero.
    output = 1
    while number > 0:

      last_digit = number % 10

      output = output * last_digit

      number = number // 10

    return output


num = int(input("Enter a number: "))
print(ProductDigits(num))
