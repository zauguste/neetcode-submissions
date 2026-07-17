from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_counter = Counter(s2[:len(s1)])
        s_counter = Counter(s1)
        if window_counter == s_counter:
            return True

        k = len(s1)
        if len(s1) == 1:
            for i in s2:
                if s1 == i:
                    return True
        
            
        for end in range(len(s2) - k):
            trailing_char = s2[end]
            leading_char = s2[end + len(s1)]
            window_counter[trailing_char] -= 1
            window_counter[leading_char] += 1
            if window_counter == s_counter:
                return True
        return False