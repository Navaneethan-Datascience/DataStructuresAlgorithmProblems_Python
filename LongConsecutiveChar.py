def LongConsecutiveChar(text):

    max_char = text[0]
    max_count = 1

    current_char = text[0]
    current_count = 1

    for i in range(1, len(text)):

        if text[i] == current_char:
            current_count += 1

        else:

            if current_count > max_count:
                max_count = current_count
                max_char = current_char

            current_char = text[i]
            current_count = 1

    # Check the last group
    if current_count > max_count:
        max_count = current_count
        max_char = current_char

    return max_char, max_count


text = "aabbbbbbcccceeecdcfc"
print(LongConsecutiveChar(text))