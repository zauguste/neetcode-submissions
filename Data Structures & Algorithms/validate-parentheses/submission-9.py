class Solution:
    def isValid(self, s: str) -> bool:
        dictClosing = {')':'(',']':'[','}':'{'}
        stack=[]
        for char in s:
            if char in dictClosing:
                if stack and stack[-1] == dictClosing[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack