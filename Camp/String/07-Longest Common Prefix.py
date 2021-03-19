'''
Question -> https://leetcode.com/problems/longest-common-prefix/
@author -> Taklemariam Alazar
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        container = dict()
        result = []
        for i in strs:
            for j in range(len(i)):
                if j not in container:
                    container[j] = [i[j], 1]
                else:
                    if container[j][0] == i[j]:
                        container[j] = [i[j], container[j][1] + 1]
        # print(container)
        for i in container.values():
            if i[1] != len(strs):
                break
            if i[1] == len(strs):
                result.append(i[0])
        # print(result)
        return "".join(result)


'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuation = {'!','?',"'",',',';','.'}
        # list(paragraph)
        z = paragraph.replace(",", " ")
        # print(z)
        para = z.split()
        new_paragraph = []
        temp = [0]
        container = dict()
        sorted_container = []
        for word in para:
            new_word = word.lower()
            for char in new_word:
                if char in punctuation:
                    temp[0] = new_word 
                    val = new_word.split(char)
                    new_val = "".join(val)
                    new_paragraph.append(new_val)
                    
            if new_word != temp[0]:
                new_paragraph.append(new_word)
        # print(new_paragraph)
        for word in new_paragraph:
            if word not in container:
                container[word] = [1, word]
            else:
                container[word] = [container[word][0] + 1, word]
        # print(container)
        for i in container.values():
            if i[1] not in banned:
                sorted_container.append(i)
        sorted_container.sort()
        result = sorted_container[-1]
        return result[1]
        
'''