class Solution:
    def findMin(self, nums: List[int]) -> int:
        # understand
        # so we have a mixed set of elements but only as two halves of a sorted array
        # and we want to get the smallest element in the array in log(n) time
        # match:
        # we can use binary search to 
        # point at the beginning middle and end of the array
        # check if the middle pivot point and the current left and right
        res = nums[0]
        left = 0
        right = len(nums)-1
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res,nums[left])
                break
            m = (left + right)//2
            res =  min(res,nums[m])
            if nums[left] <= nums[m]:
                left = m + 1
            else:
                right = m -1
        return res