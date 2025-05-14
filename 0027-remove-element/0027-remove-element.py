class Solution(object):
    def removeElement(self, nums, val):
        num=[]
        for number in nums:
            if number==val:
                continue
            num.append(number)
        n=len(nums)
        for i in range(n):
            nums.pop()
        nums.extend(num)
        return len(nums)