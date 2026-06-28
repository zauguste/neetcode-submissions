class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # What is an anagram?
        # # so all the character in s must be in t
        # how can we express that?
        # well since s must be equal to  t and the order does
        # not matter 
        # a data structure that we can use is 

        # data sturcturre: a hashamap 
        # 1. loop through all the elements
        # 2. attach the occourrence to the letter and 
        # 3. comparing the 2 results
        occurrence = dict()
        occurrencet = dict()
        for i in range(len(s)):
            occurrence[s[i]] = 1 + occurrence.get(s[i],0)
        
        for i in range(len(t)):
            occurrencet[t[i]] = 1 + occurrencet.get(t[i],0)
        return occurrence == occurrencet

            