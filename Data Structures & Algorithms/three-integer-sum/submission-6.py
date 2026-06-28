class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        re = []
        nums.sort()
        for i,a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            l,r = i + 1, len(nums) - 1
            while l < r:
                threeSums = a + nums[l] + nums[r]
                if threeSums > 0:
                    r-=1
                elif threeSums < 0:
                    l+=1
                else:
                    re.append([a,nums[l],nums[r]])
                    r-=1
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return re