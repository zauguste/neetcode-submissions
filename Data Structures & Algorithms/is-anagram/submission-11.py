class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_track = dict()
        t_track = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_track[s[i]] = 1 + s_track.get(s[i],0)
            t_track[t[i]] = 1 + t_track.get(t[i],0)
        return s_track == t_track