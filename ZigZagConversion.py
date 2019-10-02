'''
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        r=numRows
        res=''
        if (l<=r or r < 3):
            return s
        m = 0
        for i in range (0,r):
            n = i
            while (n < l):
                try:
                    res += s[n]
                except IndexError as I:
                    pass                
                if(m > 0 and  m < r-1 ):
                    try:
                        res += s [n+(2*(r-1)-(2*m))]
                    except IndexError as I:
                        pass                    
                n+=2*(r-1)                 
            m+=1
        return res

sol = Solution()
print(sol.convert("AB",1))
