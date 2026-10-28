def CountWordsFrequency(txt):

    #It splits the text and converts it into a list with separated words
    txt = txt.split(" ")

    word_count = {}

    #check the list of words in text or not and get the counts
    for word in txt:

        word_count[word] = word_count.get(word,0) + 1

    return word_count

text = "apple banana apple orange banana apple"
print(CountWordsFrequency(text))