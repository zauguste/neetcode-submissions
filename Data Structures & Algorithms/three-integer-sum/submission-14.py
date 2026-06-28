class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        #kepp going j and k arent equal because 1 number can throw off the valid array
        for i,a in enumerate(nums):

            if i > 0 and a == nums[i-1]:
                continue
            # start at the ends each time
            l, r = i+1, len(nums) - 1

            while l < r:
        # check if three is greater than 0
                if a + nums[l] + nums[r] > 0:
                    r -= 1
        # check if three is less than 0
                elif a + nums[l] + nums[r] < 0:
                    l += 1
        # add all the numbers to an array
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
        # keep for a valid by incrementung l make sure what is behind because a os nehind it 
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res