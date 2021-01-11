'''
Question -> https://leetcode.com/problems/valid-parentheses/
@Author : Taklemariam Alazar
'''
def isValid(s):
    if len(s) % 2 != 0 or ( s[0] in ")]}") or (s[-1] in "([{") :
            return False
    stack = []
    for i in range(len(s)):
        if s[i] in "([{":
            stack.append(s[i])
        else:
            if len(stack) != 0 and  (stack[-1] + s[i] == "()" or  stack[-1] + s[i] == "[]" or stack[-1] + s[i] == "{}"):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False
        
