class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort o(nlogn) time
        nums.sort()
        # 2,3,4,5,10,20
        # start at first and count up by one
        # start = 0 initially
        # largest = 0
        # large = 1 initially
        numsSet = set(nums)
        maxNum = 0
        for eachNum in numsSet:
            if eachNum - 1 not in numsSet:
                length = 1
            # then we know we have the begining of our sequence
                while (eachNum + length) in nums:
                    length += 1
            # count how long the sequence is in nums
                maxNum = max(maxNum, length)
        return maxNum