class Solution:
    def isPalindrome(self, s: str) -> bool:
        # how to figure out if something is a valid palindrome?
        # go through each caracter 
        # turn the character in to lower case each character
        # ignores all non-alphanumeric characters.
        # stack = []
        # forward = []
        # for eachCharacter in s:
        #     if eachCharacter.isalnum() or eachCharacter.isdigit():
        #         stack.append(eachCharacter.lower())

        # for eachCharacter in stack:
        #     forward.append(eachCharacter)

        # return stack == forward[::-1]

        l,r = 0,len(s)-1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1
        return True

    def alphaNum(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))
