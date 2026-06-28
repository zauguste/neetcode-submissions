class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        # initialize the left and right pointers
        l,r = 0, len(height)-1
        # keep track of the left and right 
        leftMax = height[l]
        rightMax = height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax,height[l])
                # remove the left from the window
                res += leftMax - height[l]
            else:
                r -=1
                rightMax = max(rightMax,height[r])
                # add the lagest to the window
                # remove the smallest from the window
                res += rightMax - height[r]
        return res
