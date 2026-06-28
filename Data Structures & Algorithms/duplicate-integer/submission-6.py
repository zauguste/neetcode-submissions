class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #  return True if there is a duplicate
        nSet = set()
        for i in nums:
            if i in nSet:
                return True
            nSet.add(i)
        return False