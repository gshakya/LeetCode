'''Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charIndicies ={}
        start =0
        mxLen = 0
        for curIdx in range(len(s)): 
            if (charIndicies.__contains__(s[curIdx])):
                start = charIndicies[s[curIdx]]+1 if charIndicies[s[curIdx]]+1 > start  else start
            charIndicies[s[curIdx]]=curIdx
            mxLen = curIdx-start+1 if curIdx-start+1 > mxLen else mxLen    
        return mxLen 

s = Solution()
print(s.lengthOfLongestSubstring("abecdbgabef"))