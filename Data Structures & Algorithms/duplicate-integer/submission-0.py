class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        keys = {}
        for i in nums :
            if i in keys :
                return True
            else :
                keys[i] = True
        
        return False
        