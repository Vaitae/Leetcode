class Solution(object):
    def longestCommonPrefix(self, strs):
        str=""
        for i in range(len(strs[0])):
            for s in strs:
                if i==len(s) or s[i]!=strs[0][i]:
                    return str 
            str+=s[i]
        return str       
        