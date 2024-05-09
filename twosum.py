class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        for i in range(0,n):
            for j in range(1,n):
                sum=nums[i]+nums[j]
                if sum==target:
                    print([i,j])
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        