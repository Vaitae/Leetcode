class Solution(object):
    def moveZeroes(self, nums):
        for i in nums:
            if i!=0:
                continue
            else: 
                temp=i
                nums.remove(i)
                nums.append(temp)