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
        # We don't want to have duplicate nodes
        # So, we need to keep track each node in a HashSet

        if head == None:
            return head
        
        nodeMap = {}
        
        newHead = Node(head.val)
        nodeMap[id(head)] = newHead

        if head.random :
            if id(head.random) not in nodeMap :
                nodeMap[id(head.random)] = Node(head.random.val)
            newHead.random = nodeMap[id(head.random)]

        currentNode = head
        currentNewNode = newHead

        while currentNode.next :
            currentNode = currentNode.next
            
            if id(currentNode) not in nodeMap :
                nodeMap[id(currentNode)] = Node(currentNode.val)
            currentNewNode.next = nodeMap[id(currentNode)]
            currentNewNode = currentNewNode.next

            if currentNode.random :
                if id(currentNode.random) not in nodeMap :
                    nodeMap[id(currentNode.random)] = Node(currentNode.random.val)
                currentNewNode.random = nodeMap[id(currentNode.random)]
        
        return newHead


        
            

        

        