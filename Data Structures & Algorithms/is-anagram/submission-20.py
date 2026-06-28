class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we have the strings s and t:
        # return true 
        # if the two strings are anagrams of each 
        #    both strings have the same amount of characters 

        # some strings have different order
        # but same amount of characters need to equal the same
        # What are two characters that satsfiy this condition?
        # 
        # create a table of t and s 
        # s|r:2,a:2,c:2,e:1    t|c:2,a:2,r:2,e:1
        # ---------
        # since we dont't care about the order then
        # let's compare the number of each letter
        # we can do this with a hashtable
        # t_table = {}
        # s_table = {}
        # go through s and t:
        #   build a table of s
        #   get the key if there is none default 0 add 1
        #   build a table of t
        #   get the key if there is none default 0 add 1
        # compare the values of s & t
        # if they are equal return True else: false
        t_table = {}
        s_table = {}     
        if len(s) != len(t):
            return False 
        for each_letter in range(len(s)):
            t_table[t[each_letter]] = 1 + t_table.get(t[each_letter],0)
            s_table[s[each_letter]] = 1 + s_table.get(s[each_letter],0)
        print(t_table,s_table)
        if t_table == s_table:
            return True
        else:
            return False
            
