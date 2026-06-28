class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        fre = [[] for i in range(len(nums)+1)]
        for i in nums:
            count[i] = 1 + count.get(i,0)
        for num,freq in count.items():
            fre[freq].append(num)
        
        res  = []

        for i in range(len(fre)-1,0,-1):
            for num in fre[i]:
                res.append(num)
                if len(res) == k:
                    return res
