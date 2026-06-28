class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = dict()
        tSet = dict()
        if len(s) != len(t):
            return False

        for i in range(len(s)):
           sSet[s[i]] = 1+ sSet.get(s[i],0)
           tSet[t[i]] = 1+ tSet.get(t[i],0)

        return sSet == tSet
