class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1
        while l <= r:
            if nums[l] <= target:
                if nums[l] == target:
                    return l
                l+=1
            elif nums[r] >= target:
                if nums[r] == target:
                    return r
                r-=1
        else:
            return -1
