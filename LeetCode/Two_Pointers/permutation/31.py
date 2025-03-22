# 31. Next Permutation

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]
 

class Solution(object):
    def nextPermutation(self, nums):
        ind = -1
        for i in range(len(nums)-1,-1,-1):
            if nums[i-1] < nums[i]:
                ind = i-1
                break
        if ind == -1:
            return nums.reverse()
        for i in range(len(nums)-1,-1,-1):
            if nums[ind] < nums[i]:
                nums[ind],nums[i] = nums[i],nums[ind]
                break

        nums[ind+1:] = reversed(nums[ind+1:])
        return nums
    
        
            

        
        