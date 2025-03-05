# 1480. Running Sum of 1d Array

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# BRUTE FORCE O(N^2)
class Solution(object):
    def runningSum(self, nums):
        prefix_nums = len(nums) * [0]
        for i in range(len(nums)):
            for j in range(0,i+1):
                prefix_nums[i] += nums[j]
        return prefix_nums


# PREFIX_SUM O(N)
class Solution(object):
    def runningSum(self, nums):
        prefix_nums = len(nums) * [0]
        prefix_nums[0] = nums[0]

        for i in range(1,len(nums)):
            prefix_nums[i] = prefix_nums[i-1] + nums[i]

        return prefix_nums
        