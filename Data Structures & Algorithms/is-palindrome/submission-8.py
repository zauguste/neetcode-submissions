class Solution:
    def isPalindrome(self, s: str) -> bool:
        # how to figure out if something is a valid palindrome?
        # go through each caracter 
        # turn the character in to lower case each character
        # ignores all non-alphanumeric characters.
        stack = []
        forward = []
        for eachCharacter in s:
            if eachCharacter.isalnum() or eachCharacter.isdigit():
                stack.append(eachCharacter.lower())
        print(stack)
        for eachCharacter in stack:
            forward.append(eachCharacter)
        print(forward)
        return stack == forward[::-1]