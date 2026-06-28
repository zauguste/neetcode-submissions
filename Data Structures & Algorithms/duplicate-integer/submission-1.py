class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = []
        for eachNum in nums:
            if eachNum in duplicate:
                return True
            duplicate.append(eachNum)
        return False