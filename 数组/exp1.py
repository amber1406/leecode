#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 双指针

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return nums[0:(i+1)]

s = Solution()
a = s.removeDuplicates([1,1,2])
print(a)
