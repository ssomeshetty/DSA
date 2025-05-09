# 27. Remove Element

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]

class Solution(object):
    def removeElement(self, nums, val):
        start_index = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[start_index] = nums[i]
                start_index += 1
        return start_index               
        
