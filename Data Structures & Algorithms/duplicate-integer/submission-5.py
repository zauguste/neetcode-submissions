class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkBox = set()
        for i in nums:
            if i in checkBox:
                return True

            checkBox.add(i)
        return False