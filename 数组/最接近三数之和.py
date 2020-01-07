#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    def threeSumClosest(self, nums,target):
        n=len(nums)
        nums.sort()
        result=0
        if n < 3 or not nums:
            return 0
        init_dif=abs(nums[0] + nums[1] + nums[n - 1] - target)
        for i in range(n - 2):
            l=i + 1
            r=n - 1
            while l < r:
                dif=abs(nums[i] + nums[l] + nums[r] - target)
                if dif == 0:
                    result=target
                if dif <= init_dif:
                    result=nums[i] + nums[l] + nums[r]
                    init_dif=dif
                if nums[i] + nums[l] + nums[r] - target < 0:
                    l+=1
                else:
                    r-=1
        return result
s = Solution()
print(s.threeSumClosest([0,1,2],0))