class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        subset,curset = [],[]
        nums.sort()
        def helper(i,subset,curset,nums):
            if i >= len(nums):
                subset.append(curset.copy())
                return
            # keep appending
            curset.append(nums[i])
            helper(i+1,subset,curset,nums)
            curset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            helper(i+1,subset,curset,nums)
        helper(0,subset,curset,nums)

        return subset
