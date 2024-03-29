'''
https://leetcode.com/problems/string-to-integer-atoi/
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from
this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a 
numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on
 the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists 
because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−2^31) is returned.
''' 



class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        neg=False
        if(len(str)==0):
            return 0

        if(str[0].isdigit()  or str[0] == '-' or str[0] == '+' ):
                            
            if(str[0] == '-'or str[0] == '+' ):
                try:
                    if (not str[1].isdigit()):
                        return 0
                    neg = True if str[0] =='-' else False
                    str = str[1::] 
                except IndexError as identifier:
                    return 0              
            
            mci=minCharIdx(str,0,len(str))
               
            res = int(str[0:mci])
            res = 2**31 if res >= 2**31 else res
            return -res if neg else res
        return 0
        
def minCharIdx(str: str, start: int, end: int):
    idx =(start+end)//2
    if( idx== 0):
        return len(str)
    if(idx == end and start != 0):
        return len(str)    
    leftMinIdx = min(minCharIdx(str,start,idx),idx if not str[idx].isdigit() else len(str))
    if(str[idx].isdigit()):
        return (min(leftMinIdx,minCharIdx(str,idx,end)))
    return leftMinIdx

sol = Solution()
# print(sol.myAtoi("42"))
# print(sol.myAtoi("-42"))
# print(sol.myAtoi("     -42"))
# print(sol.myAtoi("4193 with words"))
# print(sol.myAtoi("3212 "))
# print(sol.myAtoi("words and 987"))
# print(sol.myAtoi("-91283472332"))
# print(sol.myAtoi("3.14159"))
# print(sol.myAtoi(""))
# print(sol.myAtoi("+"))
print(minCharIdx("0012a42",3,7))