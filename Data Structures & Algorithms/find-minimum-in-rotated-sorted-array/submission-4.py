class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Input: nums = [3,4,5,6,1,2]
                        #|      ml r
# use binary search
# right holds the next smallest 
# mid +=1 goes to the closer half of that
# left holds the larger numbers

        l =0 
        r = len(nums)-1
        while l<r:
            m = l + ( r-l)//2
            if nums[m] < nums[r]:
                r= m
            else:
                l = m + 1
        return nums[l]
