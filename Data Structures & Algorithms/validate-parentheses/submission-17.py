class Solution:
    def isValid(self, s: str) -> bool:
        dictO = {')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if i in dictO:
                if stack and stack[-1] == dictO[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack
        