class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def recursive(curr, remaining, openCount, closeCount) :
            if remaining == 0 :
                currResult = curr
                while closeCount != openCount:
                    currResult = currResult + ")"
                    closeCount = closeCount + 1
                result.append(currResult)
                return
            
            # option 1 : decide to open new parentheses
            recursive(curr + "(", remaining - 1, openCount + 1, closeCount)

            # option 2 : decide to close parentheses
            if closeCount < openCount :
                recursive(curr + ")", remaining, openCount, closeCount + 1)
        
        recursive("(", n - 1, 1, 0)
        print(result)
        return result
