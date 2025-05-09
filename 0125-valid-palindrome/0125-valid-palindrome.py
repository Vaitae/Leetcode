class Solution(object):
    def isPalindrome(self, s):
        str=""
        for letters in s:
            if letters.isalnum():
                str+=letters.lower()
        return (str==str[::-1])