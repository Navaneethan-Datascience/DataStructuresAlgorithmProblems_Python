def VowelsConsonants(txt):

    vowels = ['a','e','i','o','u'] #vowels in alphapets

    vowel_count = 0
    consonant_count = 0

    for char in txt:
	#The loop runs until the vowel in the word in text, then if the character is a vowel, it increases the vowel count; otherwise, it increases the consonant count.
        if char in vowels:
            vowel_count = vowel_count + 1

        else:
            consonant_count = consonant_count + 1

    print("Vowel count: ", vowel_count)
    print("Consonant count: ", consonant_count)


text = "python"

print(VowelsConsonants(text))