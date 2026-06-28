class Solution:
    def isValid(self, s: str) -> bool:
        # create a ditionary and map the closing to the coresponding opening
        # remove from the stack an opening parenthesis
        # if a closing still has not been encountered keep adding

        hashmap = {')':'(', '}':'{',']':'['}
        stack = []
        for eachChar in s:
            if eachChar in hashmap:
                if stack and stack[-1] == hashmap[eachChar]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(eachChar)
        return not stack
