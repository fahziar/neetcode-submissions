class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longestConsecutive = 0

        for num in numsSet :
            currentConsecutive = 1
            currentNum = num

            while currentNum + 1 in numsSet :
                currentConsecutive += 1
                currentNum += 1
            
            longestConsecutive = max(currentConsecutive, longestConsecutive)
        
        return longestConsecutive