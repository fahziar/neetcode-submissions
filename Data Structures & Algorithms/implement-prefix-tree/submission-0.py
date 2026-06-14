class TreeNode:
    def __init__(self, val=None, end=True):
        self.val = val
        self.end = end
        self.nodes = dict()

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        currNode = self.root
        for i, char in enumerate(word) :
            if char in currNode.nodes :
                currNode = currNode.nodes[char]
            else :
                currNode.nodes[char] = TreeNode()
                currNode = currNode.nodes[char]

        if "$" not in currNode.nodes :
            currNode.nodes["$"] = TreeNode()

    def search(self, word: str) -> bool:
        currNode = self.root

        for i, char in enumerate(word) :
            print(currNode.nodes.keys())
            if char not in currNode.nodes :
                return False
            currNode = currNode.nodes[char]
        
        print(currNode.nodes.keys())
        found = "$" in currNode.nodes
        print(found)
        
        return "$" in currNode.nodes

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root

        for i, char in enumerate(prefix) :
            if char not in currNode.nodes :
                return False
            currNode = currNode.nodes[char]
        
        return True
        