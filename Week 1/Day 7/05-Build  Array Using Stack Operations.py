'''
Question -> https://leetcode.com/problems/build-an-array-with-stack-operations/
@Author -> Taklemariam Alazar
'''
def buildArray(target, n):
    n_list = [i for i in range(1,n + 1)]
    operations = []
    index = 0
    index_lis = 0
    while index < len(target):
        if n_list[index_lis] == target[index]:
            operations.append("Push")
            index += 1
            index_lis += 1
        else:
            operations = operations + ["Push", "Pop"]
            index_lis += 1
    return operations
