class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        last= (s.split(" ")[-1])
        return len(last)
        