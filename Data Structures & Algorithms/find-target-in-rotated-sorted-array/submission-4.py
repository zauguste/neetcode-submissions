class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search 
        # last is greater than prev
        # set left and right
        l = 0
        r = len(nums)-1
        while l <= r:
            # calculate the mid
            mid = (l + r)//2
            # check if we reached the mid
            if target == nums[mid]:
                return mid
            # check if less than the mid
            if nums[l] <= nums[mid]:
                # check if the last is less than the target or if target is greater than mid
                if nums[l] > target or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # missed the comparision for mid
                if nums[r] < target or target < nums[mid]:
                    r = mid - 1
                else:
                # increase the left pointer
                    l = mid + 1
        return -1
