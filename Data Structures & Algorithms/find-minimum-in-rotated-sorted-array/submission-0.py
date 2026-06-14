class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [6, 7, 1, 3, 4, 5]
        #           ^
        # how to identify minmum: check before it


        # case 1 -> minimum is at the middle
        # [6, 7, 1, 3, 4, 5]
        # 7 is not minimum, because element before it is smaller

        # case 2 -> 1 element
        # [6]
        # 6 is the minimum

        # case 3 -> the minimum is the first element
        # [1,2,3,4,5]
        # 1 is the minimum, no minimum element other than it

        # if we want to use binary search, we need to look the elemnt that
        # previous element is bigger. If not found, then the first elemnt
        # is the smallest one

        # now, how to determin whether left or right side to move
        # case 1: need to move the right side
        # [6, 7, 1, 2 ,3, 4, 5]
        #           ^

        # case 2: need to move the left side
        # [6, 7, 8, 9, 10, 1, 2]
        #           ^

        if len(nums) == 1 :
            return nums[0]   

        left = 0
        right = len(nums) - 1
        
        while left <= right :
            currIdx = (left + right) // 2
            isSmallest = False

            if currIdx == 0 :
                isSmallest = nums[currIdx] < nums[currIdx + 1]
            else :
                isSmallest = nums[currIdx] < nums[currIdx - 1]
            
            if isSmallest :
                return nums[currIdx]
            elif nums[currIdx] < nums[len(nums) - 1]:
                right = currIdx - 1
            else :
                left = currIdx + 1
        
        return -1
                