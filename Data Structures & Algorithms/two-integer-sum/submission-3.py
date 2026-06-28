class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet=dict()
        for i,x in enumerate(nums):
            # go through num set and get the index and the 
            # value
            diff = target - x
            if diff in numSet:
                # look up in constant time
                return [numSet[diff],i]
            numSet[x] = i
        