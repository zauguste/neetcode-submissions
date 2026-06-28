class Solution:
    def isValid(self, s: str) -> bool:
        # create a ditionary and map the closing to the coresponding opening
        # remove from the stack an opening parenthesis
        # if a closing still has not been encountered keep adding

        hashmap = {')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if i in hashmap:
                if stack and stack[-1] == hashmap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack
