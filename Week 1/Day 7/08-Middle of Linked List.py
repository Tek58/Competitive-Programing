'''
Question -> https://leetcode.com/problems/middle-of-the-linked-list/
@Author -> Taklemariam Alazar
'''
def middle(nums):
    slow = head
    fast = head
    while fast and fast.next != None :
        slow = slow.next
        fast = fast.next.next
    return slow