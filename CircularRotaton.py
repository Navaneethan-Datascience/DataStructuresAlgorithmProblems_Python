def CircularRotation(str1,str2):

    #checks the length of both strings also checks string2 is presenting in concatenation of two string1
    if len(str1) == len(str2) and str2 in (str1 + str1):

       return True

string1 = "ABCD"
string2 = "CDAB"
print(CircularRotation(string1,string2))
