
'''
1. split the input text into the separate words and store it as list
2. process each word in list and store it in the dictionary with count values
3. if the word exists in dictionary it adds up the count of the word
4. otherwise add the word as key in dictionary and add the count
'''
def WordFrequency(str1:str)-> dict:

    words = str1.split()

    words_cnt = {}

    for word in words:

        words_cnt[word] = words_cnt.get(word,0) + 1

    return words_cnt

print(WordFrequency("red blue red green blue red"))