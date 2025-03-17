# 42. Trapping Rain Water

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

class Solution(object):
    def trap(self, nums):
        l,r = 0,len(nums)-1

        left,right = 0,0
        res = 0
        while l<r:
            if nums[l] > left :
                left = nums[l]
            if nums[r] > right:
                right = nums[r]
            
            if left <= right:
                res += left - nums[l]
                l+=1
            else:
                res += right - nums[r]
                r-=1
        return res


        
        