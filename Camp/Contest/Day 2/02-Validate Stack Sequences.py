'''
Question -> https://leetcode.com/contest/weekly-contest-112/problems/validate-stack-sequences/
@Author -> Taklemariam Alazar
'''
class Solution:
    def validateStackSequences(self, pushed, popped):
        container = []
        pointer = 0
        for i in pushed:
            container.append(i)
            while container and pointer < len(popped) and container[-1] == popped[pointer]:
                container.pop()
                pointer += 1
        return len(container) == 0