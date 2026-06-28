class Solution:
    def isValid(self, s: str) -> bool:
        key = {')':'(',']':'[','}':'{'}
        stack = []

        for eachelement in s:
            if eachelement in key:
                # weve came across an close
                if stack and stack[-1] == key[eachelement]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(eachelement)
                # if there is nothing in the stack return 
                # true anything else return false
        return True if not stack else False
# if the stack has elements 
# and the stack top element is equal to 
# stack then keep removing elements
# ei kinda like a mirror
# else
# meaning we did not come across a stack
# then 