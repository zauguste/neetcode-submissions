class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        count = 0

        for i in numSet:
            # when to begin counting
            if (i - 1) not in numSet:
                length = 1
                while i+length in nums:
                    length +=1
                count = max(length, count)

        return count
            # when to stop
