# 922. Sort Array By Parity II

# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

# Return any answer array that satisfies this condition.

 

# Example 1:

# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
# Example 2:

# Input: nums = [2,3]
# Output: [2,3]

class Solution(object):
    def sortArrayByParityII(self, nums):
        l,r = 0,1
        while r<len(nums) and l<len(nums):
            if nums[l] % 2 == 0:
                l+=2
            elif nums[r]%2 == 1:
                r+=2
            else:
                nums[r],nums[l] = nums[l],nums[r]
                l+=2
                r+=2
            
        return nums
        