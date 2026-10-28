
'''
1. process each element in the string and store it as dictionary
2. converts dictionary pair into the single value into the list
3. join all the element in the list to the string
'''
def CompressConsecutiveChar(str1)->str:

    char_cnt = {}

    for char in str1:

        if char in char_cnt:
            char_cnt[char] += 1
        else:

            char_cnt[char] = 1

    compressed_string = []
    
    for k, v in char_cnt.items():
        
        compressed_string.append(f"{k}{v}")

    return "".join(compressed_string)

print(CompressConsecutiveChar("aaabbccccd"))