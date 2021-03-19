'''
Question -> https://leetcode.com/contest/weekly-contest-80/problems/most-common-word/
@author -> Taklemariam Alazar
'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuation = {'!','?',"'",',',';','.'}
        z = paragraph.replace(",", " ")
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