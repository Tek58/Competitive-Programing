'''
Question -> https://leetcode.com/problems/palindrome-linked-list/
@Author -> Taklemariam Alazar
'''
def isPalindrome(self, head):
    if head is None:
        return True
    placeHolder = []
    while head:
        placeHolder.append(head.val)
        head = head.next
        
    for i in range(1,len(placeHolder)+1):
        print(placeHolder[i-1], placeHolder[-i])
        if placeHolder[i-1] != placeHolder[-i]:
            return False
    return True