'''
Question -> https://leetcode.com/problems/design-linked-list/
@Author : Taklemariam Alazar
'''
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        head = self.head
        counter = 0
        while head is not None:
            if index == counter:
                return head.value
            counter += 1
            head = head.next 
        return -1
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        self.size = self.size + 1
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        

    def addAtTail(self, val: int) -> None:
        self.size = self.size + 1
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        head = self.head
        while head.next is not None:
            head = head.next
        head.next = newNode
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index > self.length():
            return
        else:
            self.size = self.size + 1
            newNode = Node(val)
            count = 0
            head = self.head
            while head.next is not None:
                if count+1 == index:
                    break
                count += 1
                head = head.next
            temp = head.next
            head.next = newNode
            newNode.next = temp
    def deleteHead(self):
        self.size = self.size - 1
        self.head = self.head.next
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.deleteHead()
        elif index >= self.length() or (index < 0):
            return 
        else:
            self.size = self.size - 1
            counter = 0
            head = self.head
            prev_node = head
            while head is not None:
                if counter == index:
                    break
                counter += 1
                prev_node = head
                head = head.next
            prev_node.next = head.next
            
    def length(self):
        return self.size