'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution:
    def reverse(self, x: int) -> int:
        
        isXNeg = False
        if (x < 0):
            isXNeg = True
        res =0 
        ip= abs(x)
        while (ip > 0):
            res = res*10+ip%10
            ip= ip//10
        
        if(res>=2**31):
            return 0
        return -res if isXNeg else res 
        
sol = Solution()
print (sol.reverse(1534236469))