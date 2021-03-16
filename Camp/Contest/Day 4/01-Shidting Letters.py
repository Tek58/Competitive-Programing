'''
Question -> https://leetcode.com/contest/weekly-contest-88/problems/shifting-letters/
@author -> Taklemariam Alazar
'''
class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        newS = list(S)
        Sum = 0
        for i in range(len(shifts)-1,-1,-1):
            Sum += shifts[i]
            val = ((ord(newS[i])-97 + Sum)%26) + 97
            newS[i] = chr(val)
        return "".join(newS)