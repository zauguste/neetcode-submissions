class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 strings
        # if anagram
        # return true
        # else return false

        # create a dictionary
        # one array count the occourence of a letter
        # one array to keep track of the coresponding

        # tacked letter until done
        # replace with a zero once found

        if len(s) != len(t):
            return False
        s_array = []
        t_array = []

        s_count = []
        s_list = []
        t_list = []

        for i in range(len(s)):
            s_array.append(s[i])
        for x in range(len(t)):
            t_array.append(t[x])
        
        for numS in range(len(s_array)):
            for numT in range(len(t_array)):
                if s_array[numS] == t_array[numT]:
                    t_array[numT] = 0
                    s_array[numS] = 0
                    break

        return t_array == s_array
                    


