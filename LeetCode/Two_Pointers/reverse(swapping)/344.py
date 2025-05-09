# 344. Reverse String

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

class Solution(object):
    def reverseString(self, nums):
        i,j = 0,len(nums)-1

        while i<=j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
        return nums
        
        