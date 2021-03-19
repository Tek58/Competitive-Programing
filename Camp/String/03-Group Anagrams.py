'''
Question -> https://leetcode.com/problems/group-anagrams/
@author -> Taklemariam Alazar
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        container = dict()
        for i in strs:
            value = self.letterToCount(i)
            if value not in container:
                container[value] = [i]
            else:
                container[value].append(i)

        return container.values()
    
    def letterToCount(self, word):
        counter_list = [0]*27
        for i in range(len(word)):
            charValue = ord(word[i]) - ord('a')
            counter_list[charValue] += 1
        return tuple(counter_list)