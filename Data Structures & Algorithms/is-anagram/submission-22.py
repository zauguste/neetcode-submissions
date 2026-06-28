class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return true if the two strings are anagrams of each other
        # otherwise return false

        # for each s and we can
        #     - reverese s and check if it is an anagram by comparing to t
        
        # since order does not matter
        # itereate over s and t using a hashmap
        # compare the value and return true if eqal and false otherwise
        hashm = {}
        hashy = {}
        for i in range(len(s)):
            hashm[s[i]] = 1 + hashm.get(s[i],0)

#s: xx
#m: x
        for i in range(len(t)):
            hashy[t[i]] = 1 + hashy.get(t[i],0)
        print(hashm,hashy)
        if hashm == hashy:
            return True
        return False