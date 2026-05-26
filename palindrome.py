def main():

    number = input("Enter a number: ")
    number = int(number)
    
    original_number = number # we store the original number because, at the end of the while loop, the "number" becomes zero
    reverse = 0	# initially, the reverse value should be zero
    while number > 0:
	#pre: it stores the original value
	#post: it becomes zero
        last_digit = number % 10 # extracts the last digit of the number
        reverse = reverse * 10 + last_digit # it update the reverse value
        number = number // 10 #removes the last digit of the number

    if original_number == reverse:
       print("The given number is palindrome",reverse)
    else:
       print("The give number is not palindrome",reverse)


if __name__ == "__main__":
    main()


'''
> before writing a program, validate the given attribute name, storing the dynamic value or static value
> understand which operators use which operation
'''