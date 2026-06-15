class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def recursive(curr, remaining, openCount, closeCount) :
            if remaining == 0 :
                currResult = curr.copy()
                while closeCount != openCount:
                    currResult.append(")")
                    closeCount = closeCount + 1
                result.append("".join(currResult))
                return
            
            # option 1 : decide to open new parentheses
            curr.append("(")
            recursive(curr, remaining - 1, openCount + 1, closeCount)
            curr.pop()

            # option 2 : decide to close parentheses
            if closeCount < openCount :
                curr.append(")")
                recursive(curr, remaining, openCount, closeCount + 1)
                curr.pop()
        
        recursive(["("], n - 1, 1, 0)
        return result
