'''
Question -> https://leetcode.com/problems/valid-anagram/
@Author : Taklemariam Alazar
'''
def isAnagram(s,t):
    anagram = False
    count = 0
    target = list(t)
    if len(s) != len(t):
        return False
    for i in s:
        for j in range(len(target)):
            if i == target[j]:
                count += 1
                target.remove(i)
                break
    if count == len(t):
        anagram = True
    return anagram