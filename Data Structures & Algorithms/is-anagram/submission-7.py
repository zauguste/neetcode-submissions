class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        if len(s)!= len(t):
            return False
        for eachChar in range(len(s)):
            sDict[s[eachChar]] = 1 + sDict.get(s[eachChar],0)
            tDict[t[eachChar]] = 1 + tDict.get(t[eachChar],0)

        return sDict == tDict