class Solution:

    def encode(self, strs: List[str]) -> str:
        emptStr = ""
        for eachStr in strs:
            emptStr += str(len(eachStr)) + '#' + eachStr
        return emptStr

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j=i
            while s[j] != '#':
                j+=1
            end = int(s[i:j])
            # go pass the delimitter
            i = j + 1
            # go pass the delimmiter and go the the end
            j = i + end
            # append the word
            res.append(s[i:j])
            # start at the new begining
            i=j
        return res