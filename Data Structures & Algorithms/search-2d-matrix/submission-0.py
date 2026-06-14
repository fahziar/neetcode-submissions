class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        rowIdx = -1

        while top <= bottom :
            currRowIdx = (top + bottom) // 2
            minVal = matrix[currRowIdx][0] #1
            maxVal = matrix[currRowIdx][len(matrix[currRowIdx]) - 1] # 7

            if minVal <= target and maxVal >= target:
                rowIdx = currRowIdx
                break
            elif minVal > target :
                bottom = currRowIdx - 1
            else :
                top = currRowIdx + 1
        
        if rowIdx == -1 :
            return False

        left = 0
        right = len(matrix[rowIdx]) - 1 #1

        while left <= right :
            currCol = (left + right) // 2 # 2

            if matrix[rowIdx][currCol] == target :
                return True
            elif matrix[rowIdx][currCol] > target :
                right = currCol - 1
            else :
                left = currCol + 1
        
        return False

    
        