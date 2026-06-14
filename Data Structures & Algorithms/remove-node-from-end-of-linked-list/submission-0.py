# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Most intuitive approach that I can think of is we have a temporarly list, preferabley array list
        # This list will hold number of element, and then we can calculate from end of the list, which element needs to be removed
        # and then we can just return head immediately

        # but, cautin if we removed the first element, then we going to replace the head

        tempList = []

        currNode = head
        tempList.append(currNode)
        while currNode.next :
            currNode = currNode.next
            tempList.append(currNode)
        
        removedPos = len(tempList) - n

        if removedPos == 0 :
            head = head.next
        else :
            if removedPos == len(tempList) - 1 :
                tempList[removedPos - 1].next = None
            else :
                tempList[removedPos - 1].next = tempList[removedPos + 1]
        
        return head
        