# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [1,2,3,4,5]
        # posToRemove = len(list) - n
        # posToRemove + n = len(list)
        #    ^          ^


        # [1,2,3,4,5]
        #    ^
        #        ^   ^

        # val = [1,2,3,4]
        # n = 4

        dummyNode = ListNode(0, head)
        left = dummyNode 
        right = head

        while right and n > 0 :
            # n = 4
            # right = 0
            right = right.next
            n -= 1
        
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummyNode.next
        