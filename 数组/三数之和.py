#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        result =  []
        if (not nums or n <3):
            return result
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                return result
            if i>0 and nums[i] == nums[i-1]:
                continue
            a = i + 1
            b = len(nums)-1
            while a<b:
                if nums[i] + nums[a] + nums[b] == 0:
                    result.append([nums[i],nums[a],nums[b]])
                    while a<b and nums[a] == nums[a+1]:
                        a += 1
                    while a<b and nums[b] == nums[b-1]:
                        b -= 1
                    a += 1
                    b -= 1
                elif nums[i] + nums[a] + nums[b] < 0:
                    a += 1
                else:
                    b -= 1
        return result
s = Solution()
print(s.threeSum([1,-1,-1,0]))
