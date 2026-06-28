class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we are given a list of integers and an number target
        # return i and j such that their values add up to the target and i cannot equal j
        num_dict = {}
        # lets keep track of all the other numbers that would possibly add up to target
        # if that number equals the target
        # if we come across that number return the value which should be the smaller index
        for index,val in enumerate(nums):
            possible_num = target - val
            if possible_num in num_dict:
                return [num_dict[possible_num], index]
            num_dict[val] = index

        