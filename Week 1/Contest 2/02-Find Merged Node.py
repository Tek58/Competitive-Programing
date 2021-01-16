'''
Questuon -> Find the node where two singly linked lists merge
@Author -> Taklemariam Alazar
'''
#Approach 1

# def findMergeNode(head1, head2):
#     temp = head1
#     while head2:
#         if head1 == head2:
#             return head1.data
#         head1 = head1.next
#         if head1 is None:    
#             head2 = head2.next
#             head1 = temp

#Approach 2 

def findMergeNode(head1, head2):
    stack1 = []
    stack2 = []
    while head1:
        stack1.append(head1)
        head1 = head1.next
    while head2:
        stack2.append(head2)
        head2 = head2.next
    res = 0

    while stack1 and stack2 and  stack1[-1] == stack2[-1]:
        res = stack1.pop().data
        stack2.pop()
    return res