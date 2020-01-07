#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
"""
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result = []
        if (not nums or n < 4):
            return result
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for b in range(i+1,n-2):
                c = b + 1
                d = n - 1
                if b > i+1 and nums[b] == nums[b-1]:
                    continue
                while c < d:
                    if nums[i] + nums[b] + nums[c] + nums[d] == target:
                        result.append([nums[i],nums[b],nums[c],nums[d]])
                        while c < d and nums[c] == nums[c+1]:
                            c += 1
                        while c < d and nums[d] == nums[d-1]:
                            d -= 1
                        c += 1
                        d -= 1
                    elif nums[i] + nums[b] + nums[c] + nums[d] < target:
                        c += 1
                    else:
                        d -= 1
        return result

s = Solution()
# print(s.fourSum([-4,-1,-1,0,1,2],0))
# print(s.fourSum([1,-2,-5,-4,-3,3,3,5],-11))
print(s.fourSum([-2,0,0,3,3,-1],5))


