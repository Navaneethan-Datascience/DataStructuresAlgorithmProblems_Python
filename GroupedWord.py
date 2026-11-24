
'''
1. Process each index of the word from the list
2. Stores each word length as dictionary key
3. stores the those words in list as values under the relavant keys.
'''

def GroupWordsLength(words:list) -> dict:

    grouped_length_of_word = {}

    for word in words:
        word_length = len(word)

        if word_length not in grouped_length_of_word:
            grouped_length_of_word[word_length] = []

        grouped_length_of_word[word_length].append(word)

    return grouped_length_of_word

print(GroupWordsLength(["cat", "dog", "apple", "tree", "sun"]))
        