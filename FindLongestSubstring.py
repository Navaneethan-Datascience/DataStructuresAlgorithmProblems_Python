
'''
1. process each character in the string
2. store unique characters in the list
2. concatenate each character into the single string
'''

def FindLongestSubstring(str1) -> int:

    if len(str1) == 1:
        return None

    unique_elements = []

    for char in str1:

        if char not in unique_elements:

            unique_elements.append(char)

    longest_substring = "".join(unique_elements)

    return longest_substring

print(FindLongestSubstring("abcabcbb"))