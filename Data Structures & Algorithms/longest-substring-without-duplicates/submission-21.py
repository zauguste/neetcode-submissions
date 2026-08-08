class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        #z,x,y,z,
        maxCount = 0#1
        # Input: s = "zxyzxyz"
                    #    |
                    # c = 0
                    # maxC = 3
                    # if alpha in set reset count
        l = 0

        alphaSet = set()

        for r in range(len(s)):
            
            while s[r] in alphaSet:
                alphaSet.remove(s[l])
                l += 1
            
            alphaSet.add(s[r])
            maxCount = max(maxCount, r - l + 1)
        
        return maxCount

