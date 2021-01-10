'''
Question -> https://leetcode.com/problems/valid-parentheses/
@Author : Taklemariam Alazar
'''
def isValid(s):
    if len(s) % 2 != 0:
        return False
    count = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if ((s[i] == "(" and s[j] == ")") or (s[i] == "[" and s[j] == "]") or (s[i] == "{" and s[j] == "}")) and ((i == j-1) or (i == ((len(s) -1) - j))):
                s = s.replace("s[j]", " ")
                count += 1
    if count == len(s)//2:
        return True
    else:
        return False
print(isValid("[[[]"))
