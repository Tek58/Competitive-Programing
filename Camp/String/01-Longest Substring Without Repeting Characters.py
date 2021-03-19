'''
Question -> https://leetcode.com/problems/longest-substring-without-repeating-characters/
@author -> Taklemariam Alazar
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        visited = set()
        first = 0
        second = 0
        while second < len(s):
            if s[second] in visited:
                maximum = max(maximum, (second - first))
                while s[first] != s[second]:
                    visited.remove(s[first])
                    first += 1
                first += 1
            visited.add(s[second])
            second += 1
        maximum = max(maximum, (second - first))
        return maximum
