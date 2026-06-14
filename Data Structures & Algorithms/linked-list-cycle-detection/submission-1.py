# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None :
            return False
        
        # Case 1 : only one node
        # Just return true
        # Case 2: when
        # Stop is when the fast pointer reach end of the list
        # or when fast pointer equal to slow pointer

        slowPointer = head
        if slowPointer.next == None :
            return False
        
        fastPointer = slowPointer.next

        while slowPointer != fastPointer and fastPointer != None :
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next

            if fastPointer != None :
                fastPointer = fastPointer.next
    
        return fastPointer != None
    

        
        