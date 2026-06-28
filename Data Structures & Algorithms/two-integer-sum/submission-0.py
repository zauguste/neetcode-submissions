class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        setOfSet = set()
        for i in range(length):
            first = nums[i]
            for n in range(1,length):
                if i == n:
                    continue
                if i != n:
                    second = nums[n]
                    sumNum = first + second
                    if sumNum == target:
                        return [i,n]