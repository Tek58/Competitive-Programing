'''
Question -> https://leetcode.com/problems/remove-linked-list-elements/
@Author -> Taklemariam Alazar
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return 
        prev = None
        while head:
            if head.val == val:
                break
            prev = head
            head = head.next
        prev.next = head.next

        