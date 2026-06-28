class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if openN < n:
        #       add open
        #  if closedN < openN:
        #       add close
        # if openN == closedN == n:
        #      return result
        stack = []
        res = []
        def backtrack(openN,closedN):

            if openN == closedN == n:
                # dont forget to append the joined stack
                res.append("".join(stack)) 
                return
            if openN < n:
                stack.append('(')
                backtrack(openN+1,closedN)
                stack.pop()
            if closedN < openN:
                stack.append(')')
                backtrack(openN,closedN+1)
                stack.pop()
        backtrack(0,0)
        # retutn the result
        return res
                