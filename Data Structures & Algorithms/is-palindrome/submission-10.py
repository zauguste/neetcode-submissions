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
        while l<r:
        #  non alpha numeric characters

            while l < r and not s[l].isalnum():
                l+=1
                # non alpha numeric characters
            while r > l and not s[r].isalnum():
                r-=1
                # is the two sides dont equal return false
            if s[l].lower() != s[r].lower():
                return False
                # if all good then keep incrementing 
            l,r = l +1,r-1    
                # we done incrementing ?
        return True