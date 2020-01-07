#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums,i,j):
            while i < j:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1
            return nums

        n = len(nums)
        k = -1
        l = -1
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                k = i
        if k == -1:
            nums.sort()
        else:
            for j in range(n):
                if nums[j] > nums[k]:
                    l = j
            if k == -1:
                nums.sort()
            else:
                nums[l],nums[k] = nums[k],nums[l]
                nums = reverse(nums,k+1,n-1)
        return nums


s = Solution()
print(s.nextPermutation([1,1,5]))