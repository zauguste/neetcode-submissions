class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sums = nums[i] + nums[j] == target: some number
        # sums == target
        # return [i,j]

        # we need to search the array for 2 numbers
        # and then we need to return their index
        # first we need to 'check if thier indicies equal each other'
        # if thery do 'continue with that number'
        # if they do not move the pointer so that both the numbers
        # equal the target and their indicies dont equal each other
         
        #  why we need to get the target

        # How do we know when to stop?

        # How do we want to start?:
            # one thing i notice is that the array is sorted
            # we can start at both ends and use a two pointer technique to check the sum
            # as we check the sum we can decide weather or not to move the two pointers
        #   based on the sum
        # How do we know when to stop?

        #   when we get a summ that equal the target return the index in an arrya like i and j
        # l,r = 0,len(nums)-1
        # while l!=r:
        #     sums = nums[l]+nums[r]
        #     if sums < target:
        #         l+1
        #     elif sums > target:
        #         r-=1
        #     else:
        #         return [0,1]
        # create a dictionsy
        # add the numbers to that dictionary and look up in constant time
        #  the number that add up to 7 by subtracting from the target

    #    7 - 3 = 4
    # need a 4
    # store 4 in some place with its index: we can use a dictionary
    # as we add to that dictionary we can 
    # check after subtracting to ensure that we did not come across the other target
    # if we did return the index of the other number\


    # #    7 - 3 = 4
    # need a key : and the index is at value
    # key = number needed and value = visited
    # visited -> 4 : 1
    # so check if what we on is what is needed
        dictionary = dict()
        for i,num in enumerate(nums):
            diff = target - num
            if diff in dictionary:
                return [dictionary[diff],i]
            dictionary[num] = i 
            




