class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        numset=set(nums)
        for i in range(n):
            nums.pop()
        numset=list(numset)
        numset.sort()
        nums.extend(numset)
        return (len(nums))