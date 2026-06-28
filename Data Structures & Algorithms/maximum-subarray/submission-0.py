class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # initialize a maxSum subarray of size 1
        maxSum = nums[0]
        # initialize a curSum 
        curSum = 0
        for n in nums:
            curSum = max(curSum,0)
            curSum+=n
            maxSum = max(curSum,maxSum)

        return maxSum