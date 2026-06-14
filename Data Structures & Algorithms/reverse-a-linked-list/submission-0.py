# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None :
            return None
        
        # plan:
        # we traverse through the list while constructing the reversed list

        reversed = ListNode(head.val)
        currNode = head

        while currNode.next != None :
            currNode = currNode.next
            newNode = ListNode(currNode.val, reversed)
            reversed = newNode

        return reversed

        
        