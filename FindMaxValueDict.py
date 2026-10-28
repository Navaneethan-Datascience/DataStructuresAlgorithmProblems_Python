
def FindMaxValueDict(dict1:dict) -> str:

    max_key = max(dict1, key=dict1.get)

    return max_key

print(FindMaxValueDict({"A": 120, "B": 450, "C": 300}))

