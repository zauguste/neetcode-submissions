class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # map the count to the given number
        fr = [[] for i in range(len(nums)+1)] # get a list of rows to put each number on
                                         # the frequency will corespond to the row number
        for c in nums:
            count[c] = 1 + count.get(c,0)
            # build the frequesncy table
        for c,i in count.items():
            fr[i].append(c)
            # append a number to its fre row
        res = []
        for i in range(len(fr)-1,0,-1):
            for num in fr[i]:
                res.append(num)
                if len(res) == k:
                    return res