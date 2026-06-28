class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # gives temperatures 
        # each temp has a corresponding day
        # this is a monotonic stack
        
        # each temperature is a monotonic stack input
        res = [0] * len(temperatures)
        stack = []
        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp,stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((temp,i))

        return res