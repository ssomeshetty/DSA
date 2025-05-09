# 75. Sort Colors
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

class Solution(object):
    def sortColors(self, nums):
        i,j,k = 0,0,len(nums)-1
        while j<=k:
            if nums[j] == 0:
                nums[j],nums[i] = nums[i],nums[j]
                j+=1
                i+=1
            elif nums[j] == 1:
                j+=1
            else:
                nums[j],nums[k] = nums[k],nums[j]
                k-=1
                
        return nums
        # l,m,n = 0,0,len(nums)-1
        # while m<=n:
        #     if nums[m] == 0:
        #         nums[l] ,nums[m] = nums[m],nums[l]
        #         l+=1
        #         m+=1
        #     elif nums[m] == 1:
        #         m+=1
        #     else:
        #         nums[n],nums[m] = nums[m],nums[n]
        #         n-=1
        # return nums

        # return nums.sort()

        # cnt0 ,cnt1,cnt2 = 0,0,0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         cnt0 += 1 
        #     elif nums[i] == 1:
        #         cnt1 += 1
        #     else:
        #         cnt2 += 1
        # for i in range(cnt0):
        #     nums[i] = 0
        # for i in range(cnt0,cnt0+cnt1):
        #     nums[i] = 1
        # for i in range(cnt0+cnt1,cnt0+cnt1+cnt2):
        #     nums[i] = 2
        # return nums

        # low,mid = 0,0
        # high = len(nums) - 1
        # while mid <= high:
        #     if nums[mid] ==  0:
        #         # Datch National Flag Algorithm
        #         nums[mid],nums[low] = nums[low],nums[mid]
        #         mid += 1
        #         low += 1
        #     elif nums[mid] == 1:
        #         mid += 1
        #     else:
        #         nums[mid],nums[high] = nums[high],nums[mid]
        #         high -= 1
        # return nums

