class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #loop through the length of the
        # s and t string
        # map their corresponding elements
        dictT = {}
        dictS = {}
        for i in s:
            dictS[i] = 1 + dictS.get(i,0)
        for i in t:
            dictT[i] = 1 + dictT.get(i,0)
        return dictT == dictS