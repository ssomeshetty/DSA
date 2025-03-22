# 556. Next Greater Element III

# Example 1:

# Input: n = 12
# Output: 21
# Example 2:

# Input: n = 21
# Output: -1
 

class Solution(object):
    def nextGreaterElement(self, n):
        nums = []
        ind = -1
        while n > 0:
            rem = n%10
            nums.append(rem)
            n = n/10
        nums.reverse()
        for i in range(len(nums)-1,-1,-1):
            if nums[i-1] < nums[i]:
                ind = i-1
                break
        if ind == -1:
            return -1
        for i in range(len(nums)-1,ind,-1):
            if nums[ind] < nums[i]:
                nums[ind],nums[i] = nums[i],nums[ind]
                break
        # if len(nums) > 2:
        nums[ind+1:] = reversed(nums[ind+1:])
        num = int("".join(map(str,nums)))
        return num if num < (2**31) else -1   
        
        