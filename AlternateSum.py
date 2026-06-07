def AlternateSum(n):

    sum = 0

    #numbers are adding if the number is odd, subtracting if the number is even 
    for i in range(1,n+1):

        if i % 2 == 0:

           sum = sum - i

        else:

           sum = sum + i

    return sum

number = int(input("Enter a number: "))
print(AlternateSum(number))