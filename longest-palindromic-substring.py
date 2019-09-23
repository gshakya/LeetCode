'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

https://leetcode.com/problems/longest-palindromic-substring/
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        es = "#"
        for chr in s: 
            es += chr+"#"
        p = []
        c=0
        maxPos = 0
        maxVal = 0
        while (c < len(es)):
            l=c
            r=c
            if(c==0 or c == len(es)-1):
                p.append(0)
            else:
                while (l>-1 and r<len(es) and es[l]==es[r]):
                    l-=1
                    r+=1
                if((int((r-l)/2)-1)>maxVal):
                    maxVal = int((r-l)/2)-1
                    p.append(maxVal)
                    maxPos = c
            c+=1

        start = maxPos - maxVal
        end = maxPos + maxVal
        res = es[start:end+1]
        
        return(res.replace('#',''))


sol = Solution()
print(sol.longestPalindrome("acncacn"))
