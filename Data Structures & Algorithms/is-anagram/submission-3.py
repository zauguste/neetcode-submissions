class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        if len(s) != len(t):
            return False
        for i in s:
            dictS[i] = 1 + dictS.get(i,0)
        for i in t:
            dictT[i] = 1 + dictT.get(i,0)
        return dictT == dictS
            