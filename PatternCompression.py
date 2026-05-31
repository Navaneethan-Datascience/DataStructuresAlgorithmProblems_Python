def PatternCompression(txt):

    result = ""
    count = 1

    for i in range(1,len(txt)):

        if txt[i] == txt[i-1]:

           count = count + 1

        else:

           result += txt[i-1] + str(count)
           count = 1

    result += txt[-1] + str(count)


    return result


string = "aaabbc"
print(PatternCompression(string))

        

        