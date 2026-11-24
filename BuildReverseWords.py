'''
1. Process each value string from the dictionary split that string and store it as list of values
2. Process each index document from the list
3. If the index document is in the desired dictionary store the append the relavant key as value; otherwise store a new key as values for new index document
'''


def BuildReverseWords(dict1:dict) -> str:

    document_ids = {}

    for key, value in dict1.items():

        for document in list(value.split(" ")):

            if document not in document_ids: 

                document_ids[document] = [key]

            else:

                document_ids[document].append(key)

    return document_ids

print(BuildReverseWords({"D1":"python data","D2":"data science","D3":"python science"}))