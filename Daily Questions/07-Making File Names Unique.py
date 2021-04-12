'''
Question -> https://leetcode.com/problems/making-file-names-unique/
@Author -> Taklemariam Alazar
'''
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        container = dict()
        result = []
        for name in names:
            if name not in container:
                container[name] = [name, 1]
            else:
                value = container[name]
                index = value[1]
                newName = value[0] + "("+str(index)+")"
                while newName in container:
                    index += 1
                    newName =  value[0] + "("+str(index)+")"
                    container[name] = [value[0], index]
                container[newName] = [newName, 1]
        for i in container.keys():
            result.append(i)
        
        return result