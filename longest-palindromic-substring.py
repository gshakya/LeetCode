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
        if len(s) < 2:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        
        es ='#'+'#'.join('{}'.format(s))+'#'
       
        N = len(es)
        p = [0]*N
              
        C=0
        R=0
        maxLen=0
        mirror =0
        pC=0
        for i in range(0,N):
            mirror = 2*C -i
            if (i < R ):
                p[i]= min(p[mirror],R-i)
                
            r=i + (1 + p[i])
            l=i - (1 + p[i])
               
            try:
                while (es[l]==es[r]):
                    l-=1
                    r+=1
                    p[i]+=1
            except IndexError as e: 
                pass
            if(i+p[i]>R):
                C,R = i,p[i]+i
                
            if(p[i]>maxLen):
                pC =i    
                maxLen = p[i]
                
        return(s[(pC-maxLen)//2:(pC+ maxLen)//2])


sol = Solution()
print(sol.longestPalindrome("babad"))
