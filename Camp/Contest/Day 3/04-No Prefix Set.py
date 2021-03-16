'''
Question -> https://www.hackerrank.com/contests/a2sv-contest-8/challenges/no-prefix-set/problem
@author -> Taklemariam Alazar
'''
class Node:
    def __init__(self):
        self.children = [None] * 10
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = Node()
    
    def getIndex(self,letter):
        return ord(letter) - ord("a")

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if curr.isEnd:
                return True
            indexChar = self.getIndex(char)
            if curr.children[indexChar] == None:
                curr.children[indexChar] = Node()
            
            curr = curr.children[indexChar]
                
        if curr.isEnd:
            return True
        
        for child in curr.children:
            if child is not None:
                return True
                
        curr.isEnd = True
        return False
        

def noPrefix(words):
    obj = Trie()
    for word in words:
        if obj.insert(word):
            print("BAD SET")
            print(word) 
            return
    print("GOOD SET")