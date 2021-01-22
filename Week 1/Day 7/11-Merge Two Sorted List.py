'''
Question -> https://leetcode.com/problems/merge-two-sorted-lists/
@Author -> Taklemariam Alzar
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(self, l1: ListNode, l2: ListNode) :
    if not l1:
        return l2
    elif not l2:
        return l1
    elif not l1 and not l2:
        return 
    sorted_list1 = []
    sorted_list2 = []
    list_node = ListNode()
    while l1 :
        sorted_list1.append(l1.val) 
        l1 = l1.next
    while l2 :
        sorted_list2.append(l2.val) 
        l2 = l2.next
    result = sorted(sorted_list1 + sorted_list2)
    list_node = value =  ListNode(0)
    for i in result:
        list_node.next = ListNode(i)
        list_node = list_node.next
    return value.next