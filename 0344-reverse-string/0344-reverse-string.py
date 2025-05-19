class Solution(object):
    def reverseString(self, s):
        res=s[::-1]
        n=len(s)
        for c in range(n):
            s.pop()
        s.extend(res)
        print(s)
        