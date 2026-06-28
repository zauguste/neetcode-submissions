class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for i in range(len(nums)+1)]
        count = dict()
        for i in nums:
            count[i] = 1 + count.get(i,0)
        for n,freq in count.items():
            res[freq].append(n)
        output = []
        for i in range(len(res)-1,0,-1):
            for x in res[i]:
                output.append(x)
                if len(output) == k:
                    return output