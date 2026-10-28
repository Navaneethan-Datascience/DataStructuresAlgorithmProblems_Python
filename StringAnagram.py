
'''
1. Process each element from the word
2. count that element frequency
3. store that as dictionary values
'''
def StringAnagram(str1,str2)-> bool:

    #normalize the input before counting the words
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()

    char_cnt_str1 = {}
    char_cnt_str2 = {}

    for char1 in str1:

        if char1 in char_cnt_str1:

            char_cnt_str1[char1] += 1

        else:

            char_cnt_str1[char1] = 1


    for char2 in str2:
    
            if char2 in char_cnt_str2:
    
                char_cnt_str2[char2] += 1
    
            else:
    
                char_cnt_str2[char2] = 1

    return char_cnt_str1 == char_cnt_str2

print(StringAnagram("Tea","eat"))

