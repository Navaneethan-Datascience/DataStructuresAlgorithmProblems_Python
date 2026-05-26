def main():

    string = input('Enter a string: ')

    char_count = {}

    # Count characters
    for char in string:

        char_count[char] = char_count.get(char, 0) + 1

    # Find first non-repeating character
    for char in string:

        if char_count[char] == 1:

            print(char)
            return

    print("No non-repeating character found")

if __name__ == "__main__":
    main()