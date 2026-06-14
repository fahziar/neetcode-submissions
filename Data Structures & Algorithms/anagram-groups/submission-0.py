from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []

        while len(strs) != 0 :
            currList = []
            currStr = strs.pop(0)
            currList.append(currStr)

            j = 0
            while j < len(strs) :
                if self.isAnagram(currStr, strs[j]) :
                    currList.append(strs.pop(j))
                else :
                    j += 1
            
            output.append(currList)
        return output
    
    def isAnagram(self, a : str, b : str) -> bool:
        if len(a) != len(b) :
            return False
        
        countA, countB = defaultdict(int), defaultdict(int)

        for i in range(0, len(a)) :
            countA[a[i]] += 1
            countB[b[i]] += 1
        
        return countA == countB
