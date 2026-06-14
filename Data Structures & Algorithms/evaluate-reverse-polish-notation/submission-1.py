class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens :
            # stack = [10 6 -132]
            if token not in ('+', '-', '*', '/') :
                stack.append(int(token))
            else :
                secondToken = stack.pop() # -11
                firstToken = stack.pop() # 12

                if token == '+' :
                    stack.append(firstToken + secondToken)
                elif token == '-' :
                    stack.append(firstToken - secondToken)
                elif token == '*' :
                    stack.append(firstToken * secondToken)
                elif token == '/' :
                    stack.append(int(firstToken / secondToken))
        
        return stack.pop()
        