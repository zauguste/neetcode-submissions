class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ''
        for i in strs:
            newString += str(len(i)) + '#' + i
        return newString
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
                # 4#neeet
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res



