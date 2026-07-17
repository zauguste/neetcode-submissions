class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        end = 0
        start = 0
        max_num = 0
        max_arr = []
        # if k == 1:
        #     for i in nums:
        #         max_arr.append(i)
        #     return max_arr
        
        for end in range(len(nums)- k +1):
            # start our window at end end our endow and end + k
            max_num = max(nums[end:end + k])
            max_arr.append(max_num)
        return max_arr