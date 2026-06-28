class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair : [temp,index]

        for i,temp in enumerate(temperatures):
            # is our stack empty and is the temp greater than 
            # what is on the top of our stack. The top of our stack is stack[-1] the temp is the 
            # first value in that pair
            while stack and temp > stack[-1][0]:
                # pop from our stack the temp and index
                stackT, stackInd = stack.pop()
                # for this temp in the result output whatever the result of stack index
                # we want to compute the number of days it took us to find a greater temp

                res[stackInd] = (i - stackInd)

            stack.append([temp,i])
        return res
