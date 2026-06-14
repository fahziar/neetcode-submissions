class PrefixTree:

    def __init__(self):
        self.root = dict()
        

    def insert(self, word: str) -> None:
        currNode = self.root
        for char in word:
            if char not in currNode :
                currNode[char] = dict()
            currNode = currNode[char]
        
        currNode["$"] = dict()

    def search(self, word: str) -> bool:
        currNode = self.root
        for char in word :
            if char not in currNode :
                return False
            currNode = currNode[char]

        return "$" in currNode        

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for char in prefix :
            if char not in currNode :
                return False
            currNode = currNode[char]
        
        return True
        
        