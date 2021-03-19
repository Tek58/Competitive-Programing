'''
Question -> https://leetcode.com/contest/weekly-contest-80/problems/linked-list-components/
@author -> Taklemariam Alazar
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        counter = 0
        isConnected = False
        container = set(G)
        while head:
            if head.val in G:
                isConnected = True
            else:
                if isConnected:
                    counter += 1
                    isConnected = False

            head = head.next
        if isConnected:
            return counter + 1
            
        return counter