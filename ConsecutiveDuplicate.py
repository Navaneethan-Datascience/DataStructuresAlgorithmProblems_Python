def ConsecutiveDuplicate(txt):

    char = ""
    
    #compares the current element and the next element in text, if they're not the same, it adds the concatenation of the elements.
    for i in range(len(txt)-1):

        if txt[i] != txt[i+1]:

           char = char + txt[i]

    return char


string = "aaabbccdaa"
print(ConsecutiveDuplicate(string))