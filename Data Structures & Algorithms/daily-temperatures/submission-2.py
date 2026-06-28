class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures): #go through the temperatures and their days
            while stack and temp > stack[-1][0]: #continuously remove the larger number to keep a monotonic stack
                stackT,stackI = stack.pop()
                res[stackI] = i - stackI #subtract the index to get the amount of days for each number that we've poped
            stack.append((temp,i)) #append the temp and day
        return res