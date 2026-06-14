class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for row in range(0, 9) :
            usedNumber = set()
            for column in range(0,9) :
                if board[row][column] != '.' and board[row][column] in usedNumber :
                    return False
                usedNumber.add(board[row][column])
        
        # check column
        for column in range(0, 9) :
            usedNumber = set()
            for row in range(0,9) :
                if board[row][column] != '.' and board[row][column] in usedNumber :
                    return False
                usedNumber.add(board[row][column])
        
        # check sub-boxes
        for boxRow in range(0, 3) :
            for boxColumn in range (0, 3) :
                usedNumber = set()
                for row in range(0, 3) :
                    currRow = (boxRow * 3) + row
                    for column in range(0, 3) :
                        currColumn = (boxColumn * 3) + column
                        if board[currRow][currColumn] != '.' and board[currRow][currColumn] in usedNumber :
                            return False
                        usedNumber.add(board[currRow][currColumn])
        return True

        