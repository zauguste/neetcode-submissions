class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffDict = dict()
        for i,num in enumerate(nums):
            diff = target - num
            if diff in diffDict:
                return [diffDict[diff],i]
            diffDict[num] = i