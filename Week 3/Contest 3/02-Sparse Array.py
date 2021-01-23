'''
Question -> Matching Array
@Author -> Taklemariam Alazar
'''
def matchingStrings(strings, queries):
    result = []
    for i in queries:
        count = 0
        for j in strings:
            if i == j:
                count += 1
        result.append(count)
    return result