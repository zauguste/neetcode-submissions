class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            # create an unique set of values using the amount of char in the alpabet
            count = [0] * 26
            for char in i:
                # update position value
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(i)
        return res.values()

