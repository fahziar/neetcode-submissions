# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None :
            return list2
        if list2 == None :
            return list1
        
        head = None
        currList1 = list1
        currList2 = list2
        
        if currList1.val > currList2.val :
            head = ListNode(currList2.val, None)
            currList2 = currList2.next
        else :
            head = ListNode(currList1.val, None)
            currList1 = currList1.next
        currNode = head

        while currList1 != None or currList2 != None :
            if currList2 == None :
                currNode.next = currList1
                currList1 = None
            elif currList1 == None :
                currNode.next = currList2
                currList2 = None
            else :
                if currList1.val > currList2.val :
                    currNode.next = ListNode(currList2.val)
                    currNode = currNode.next
                    currList2 = currList2.next
                else :
                    currNode.next = ListNode(currList1.val)
                    currNode = currNode.next
                    currList1 = currList1.next
        
        return head

        