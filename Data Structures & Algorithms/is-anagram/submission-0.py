from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        
        usedChar = defaultdict(int)
        
        for c in s :
            usedChar[c] += 1
        
        for c in t :
            usedChar[c] -= 1
        
        for c in usedChar :
            if usedChar[c] != 0 :
                return False
        
        return True
            
        return True