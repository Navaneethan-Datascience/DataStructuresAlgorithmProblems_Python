def Anagram(str1, str2):

    if len(str1) != len(str2):
       return False
    
    # Anagram: Two words are anagrams if they contain the same characters in different order.
    str1 = sorted(str1)
    str2 = sorted(str2)

    if str1 == str2:
       return True
    else:
       return False

string1 = input("Enter a first word: ")
string2 = input("Enter a first word: ")
print(Anagram(string1,string2))