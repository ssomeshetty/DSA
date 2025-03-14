# 11. Container With Most Water

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

class Solution(object):
    def maxArea(self, nums):
        i,j = 0,len(nums)-1
        res = 0
        while i < j:
            area = min(nums[i],nums[j]) * (j-i)
            res = max(res,area)
            if nums[i] < nums[j] :
                i+=1
            else:
                j-=1
        return res
    
    
class Solution(object):
    def maxArea(self, nums):
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                min_ = min(nums[i],nums[j])
                product = min_ * (j-i)
                if product > ans:
                    ans = product
        return ans     
        