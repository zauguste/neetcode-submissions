class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [2,20,4,10,3,4,5]
        numSet = set(nums)
        maxLong =0
        for i in numSet:
            if (i-1) not in numSet:
                # count the longest
                longest = 1
                while (i+longest) in numSet:
                    longest+=1
                maxLong = max(longest,maxLong)
        return maxLong
