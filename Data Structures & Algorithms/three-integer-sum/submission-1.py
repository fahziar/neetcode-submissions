class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        
        # [-4, -1, -1,0,1,2]

        for i in range(0, len(nums) - 2) :
            # i = 0
            j = i + 1  # j = 1
            k = len(nums) - 1 # k = 5
            while j < k :
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0 :
                    result.add((nums[i], nums[j], nums[k]))
                    k -= 1
                elif sum < 0 :
                    j += 1
                else :
                    k -= 1
        
        return [list(combination) for combination in result]
                