class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair : [temp,index]

        for i,t in enumerate(temperatures):
            # if the stack not empty and the temperature is greater than the top

            while stack and t > stack[-1][0]:
                # remove from the top of the stack
                stackT,stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append((t,i))
        return res