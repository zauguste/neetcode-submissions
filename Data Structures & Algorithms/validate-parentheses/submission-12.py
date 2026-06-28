class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dicClosing = {')':'(','}':'{',']':'['}
        for eachChar in s:
            if eachChar in dicClosing:
                if stack and stack[-1] == dicClosing[eachChar]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(eachChar)
        return not stack # the stack is not empty ? True