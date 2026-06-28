class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if n = 1 return '()'
        # if open parenthesis < n
        # add a open
        # if closed parenthesis < open parenthesis
        # add a closed parenthesis
        # if closed == open == n:
        # return the result

        stack = [] 
        result = []
        if n == 1:
            return ['()']
        def backtrack(openN,closeN):
            if openN == closeN == n:
                result.append(''.join(stack))
                return
            if openN < n:
                stack.append('(')
                backtrack(openN+1,closeN)
                stack.pop()
            if closeN < openN:
                stack.append(')')
                backtrack(openN,closeN+1)
                stack.pop()
        backtrack(0,0)
        return result