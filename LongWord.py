def LongWord(txt):

    value = txt.split(" ") #splits the words in the sentence by using delimiter

    word_length = {} #empty dictionary to store the word and word length.
    """
    Checks the 'txt' value available in a list. If it is available, it stores the word and that length as a key-value pair
    It identifies the longest word length, then it prints that value.
    """
    for txt in value:

        word_length[txt] = len(txt)

    long_len_word = max(word_length, key = word_length.get)
    print(long_len_word,"-->",word_length[long_len_word])
	
    return word_length


text = "How that person add value in my life"

print(LongWord(text))