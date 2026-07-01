class Solution:
    # [0, 1, 2]
    # 
    def canJump(self, nums: List[int]) -> bool:
        reachable = [False for i in nums]
        for i in range(len(nums) - 1, -1, -1) :
            if i + nums[i] + 1 >= len(nums) :
                reachable[i] = True
            else :
                for j in range(i, i + nums[i] + 1) :
                    if reachable[j]:
                        reachable[i] = True
                        break
        
        return reachable[0]
        