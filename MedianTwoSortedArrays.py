import math 
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mLow= math.floor((len(nums1)+len(nums2)+1)/2)-1
        mHigh=math.ceil((len(nums1)+len(nums2)+1)/2)-1
        i =0
        cn1 =0
        cn2=0
        median = 0
        while(i <= mHigh and mLow>=0 and mHigh>=0):
            if(cn1 > (len(nums1)-1)):
                if(i==mLow):
                    median= nums2[cn2]
                if(i==mHigh):
                    median+= nums2[cn2]
                cn2+=1
            
            elif(cn2 > (len(nums2)-1)):
                if(i==mLow):
                    median= nums1[cn1]
                if(i==mHigh):
                    median+= nums1[cn1]
                cn1+=1
            
            elif(nums1[cn1]<nums2[cn2]):
                if(i==mLow):
                    median= nums1[cn1]
                if(i==mHigh):
                    median+= nums1[cn1]
                cn1+=1

            else:
                if(i==mLow):
                    median= nums2[cn2]
                if(i==mHigh):
                    median+= nums2[cn2]
                cn2+=1
            i+=1
        return 0 if median == 0 else median/2

s = Solution()
print(s.findMedianSortedArrays([1,2],[3,4]))