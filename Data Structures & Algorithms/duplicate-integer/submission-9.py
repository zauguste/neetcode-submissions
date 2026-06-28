class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set() #1,2,3

        for numbers in nums: #on: 1,2,3,3
            if numbers in num_set: #if 1 in num_set? no,is 2 in num_set? no,is 3 in num_set? No,is 3 in num_set? yes
                return True
            num_set.add(numbers) #add 1,add 2,add 3
        return False
