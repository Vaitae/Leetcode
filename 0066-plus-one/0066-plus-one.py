class Solution(object):
    def plusOne(self, digits):
        n=len(digits)
        num=""
        for i in digits:
            i=str(i)
            num+=i
        num=int(num)
        num=num+1
        for i in range(n):
            digits.pop()
        num=str(num)
        for i in num:
            i=int(i)
            digits.append(i)
        return digits
        