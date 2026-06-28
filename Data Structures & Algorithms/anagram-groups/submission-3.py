class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for eachstring in strs:
            count = [0] * 26
            for s in eachstring:
                count[ord(s) - ord('a')] += 1
            res[tuple(count)].append(eachstring)
        return res.values()