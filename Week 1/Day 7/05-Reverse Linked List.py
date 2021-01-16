def reverseList(self, head):
        if head is None:
            return
        return self.helper(head)[1]
    
def helper(self, head):
    if (head.next == None):
        return head, head
    newHead, tail = self.helper(head.next)
    newHead.next = head
    head.next = None
    return head, tail