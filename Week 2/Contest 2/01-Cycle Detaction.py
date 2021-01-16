'''
Questuon -> Find the node where two singly linked lists merge
@Author -> Taklemariam Alazar
'''

#Approach 1
# def has_cycle(head):
#     if head.next is None:
#         return 0
#     store = []
#     while head:
#         if head in store:
#             return 1
#         store.append(head)
#         head = head.next
#     return 0

#Approach 2
def has_cycle(head):
    if head is None or head.next is None:
        return 1
    
    fast = head.next
    slow= head
    while slow != fast:
        if fast is None or fast.next is None:
            return 0
        fast = fast.next.next
        slow = slow.next
    return 1