class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first we want to count the number of elements
        # then we want to get the most frequent
        # we can map its frequency to an index
        #so nums[1]
        freq = [[] for i in range(len(nums)+1)]
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        for count,freqs in count.items():
            freq[freqs].append(count)
        res = []
        for i in range(len(freq)-1,0,-1):
            for x in freq[i]:
                res.append(x)
                if len(res) == k:
                    return res

