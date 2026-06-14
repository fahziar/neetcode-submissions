# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currL1 = l1
        currL2 = l2
        mantissa = 0
        head = None

        while currL1 != None or currL2 != None :
            if currL1 == None :
                l1Val = 0
            else :
                l1Val = currL1.val
            
            if currL2 == None :
                l2Val = 0
            else :
                l2Val = currL2.val

            sum = l1Val + l2Val + mantissa
            mantissa = sum // 10
            sum = sum % 10

            if head == None :
                head = ListNode(sum)
                curr = head
            else :
                curr.next = ListNode(sum)
                curr = curr.next
            
            if currL1 != None :
                currL1 = currL1.next
            
            if currL2 != None :
                currL2 = currL2.next
        
        if mantissa != 0 :
            curr.next = ListNode(mantissa)

        return head
            


        