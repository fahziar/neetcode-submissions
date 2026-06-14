"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head == None :
            return head
        
        nodeMap = {}

        newHead = Node(head.val)
        nodeMap[head] = newHead

        if head.random != None :
            if head.random not in nodeMap :
                nodeMap[head.random] = Node(head.random.val)
            newHead.random = nodeMap[head.random]
        
        currNode = head
        currNewNode = newHead

        while currNode.next != None :
            currNode = currNode.next

            if currNode not in nodeMap :
                nodeMap[currNode] = Node(currNode.val)
            currNewNode.next = nodeMap[currNode]
            currNewNode = currNewNode.next

            if currNode.random != None :
                if currNode.random not in nodeMap :
                    nodeMap[currNode.random] = Node(currNode.random.val)
                currNewNode.random = nodeMap[currNode.random]
        
        return newHead
        