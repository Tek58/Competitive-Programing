'''
Question -> https://leetcode.com/problems/implement-queue-using-stacks/
@Author -> Taklemariam Alazar
'''
class MyQueue:

    def __init__(self):
        self.value = []
        self.size = 0
        

    def push(self, x: int) -> None:
        self.size = self.size + 1
        self.value.append(x)
        

    def pop(self) -> int:
        if self.size == 0:
            return
        self.size = self.size - 1
        val = self.value[0]
        self.value = self.value[1:]
        return val
        

    def peek(self) -> int:
        return self.value[0]
        
    def empty(self) -> bool:
        if self.size == 0:
            return True
        return False