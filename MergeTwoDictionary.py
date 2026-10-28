'''
1. Condition checks if the key is in the dictionary 1 and dictionary 2 or not; if it is adds those two common keys relavant values
2. other wise assign the same values from dictionary 1
3. if key in dictionary 2 and not in the final dictionary; the final dictionary that particular keys and values
'''



def MergeTwoDictionary(dict1:dict,dict2:dict) -> dict:

    merged_dict = {}

    for key in dict1:

        if key in dict2:

            merged_dict[key] = dict1[keys] + dict2[key]

        else:

            merged_dict[key] = dict1[key]

    for key in dict2:

        if key not in merged_dict:

            merged_dict[key] = dict2[key]

    return merged_dict

print(MergeTwoDictionary({"apple": 10, "banana": 20},{"banana": 15, "orange": 30}))