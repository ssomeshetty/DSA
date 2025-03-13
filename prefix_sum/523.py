# 523. Continuous Subarray Sum

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# Example 2:

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false  

# Optimal Approach 

class Solution(object):
    def checkSubarraySum(self, nums, k):
        hashmap = {}
        s = 0
        for i,n in enumerate(nums):
            s += n

            s = s % k

            if s == 0 and i >= 1:
                return True
            
            if s not in hashmap:
                hashmap[s] = i
            else:
                idx = hashmap[s]
                if i-idx >= 2:
                    return True
        return False
    

# My Approach   Not passed all the test cases 80/100

class Solution(object):
    def checkSubarraySum(self, nums, k):
        hashmap = {}
        s = 0
        flag = None
        cnt = 0
        if len(nums) <= 1:
            return False
        for n in nums:
            if n==0:
                cnt += 1
        if cnt >= 2:
            flag = True
        
        for i , n in enumerate(nums):
            s += n
            value = s-k
            if s%k == 0:
                if i >= 1:
                    flag = True
                
            elif value in hashmap :
                idx = i - hashmap[value]
                if idx >= 2:
                    flag = True
                if idx < 2 and flag != True:
                    flag = False
            if s not in hashmap:
                hashmap[s] = i
        if s%k != 0 and flag == None:
            flag = False

        return flag
