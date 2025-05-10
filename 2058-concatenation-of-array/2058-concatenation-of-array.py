class Solution(object):
    def getConcatenation(self, nums):
        res=[]
        for i in range(2):
            for num in nums:
                res.append(num)
        return res
        