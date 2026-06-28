class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dicClos = {')':'(','}':'{',']':'['}
        for o in s:
            if o in dicClos:
                if stack and stack[-1] == dicClos[o]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(o)
        return not stack