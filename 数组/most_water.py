#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    def maxArea(self, height):
        result = 0
        i = 0
        j = len(height)-1
        while True:
            area = (j-i)*min(height[i],height[j])
            if area > result:
                result = area
            if i == j:
                break
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return result

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))


        # result = 0
        # for i in range(len(height)-1):
        #     for j in range(1,len(height)):
        #         area = (j-i)*min(height[i],height[j])
        #         if area > result:
        #             result = area
        # return result
