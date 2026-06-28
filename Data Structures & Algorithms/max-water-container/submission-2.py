class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # initialize a left and right
        l,r = 0,len(heights)-1
        maxA = 0
        while l< r:
            minA = min(heights[l],heights[r]) * (r-l)
            maxA = max(minA,maxA)
            if heights[l]<= heights[r]:
                l+=1
            else:
                r-=1
        return maxA