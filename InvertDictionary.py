'''
1. reads each key and values in a defined dictionary
2. in a defined empty dictionary store 'value' as 'key'; 'key' as value
'''

def InvertDictionary(dict1:dict) -> dict:

    inverted_dictionary = {}

    for keys, values in dict1.items():

        inverted_dictionary[values] = keys

    return inverted_dictionary


print(InvertDictionary({"a": 1, "b": 2, "c": 3}))