def NumberPyramidSum(n):

    sum = 0

    for i in range(1,n+1):

        row_tot = 0

        for j in range(1,i+1):

            row_tot = row_tot + j

        sum = sum + row_tot

    return sum

number = int(input("Enter a number: "))
print(NumberPyramidSum(number))