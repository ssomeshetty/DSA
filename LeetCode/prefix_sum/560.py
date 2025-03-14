# 560. Subarray Sum Equals K

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

# Example 3 :

# nums = [1] , k = 0     here u see , when we apply sliding window approach than here it fails , because when 0 or any negative numbers comes it fails 
# Output = 0             EX : [1,2,3,6,0,0,4] see subarray can takes 0,0 means 4th and 5th index values also . but in sliding window its not possible .


# BRUTE FORCE

class Solution(object):
    def subarraySum(self, nums, k):
        res = 0
        for i in range(len(nums)):
            Sum = 0
            for j in range(i,len(nums)):
                Sum += nums[j]
                if Sum == k:
                    res += 1

        return res
    
#OPTIMAL APPROACH 

class Solution(object):
    def subarraySum(self, nums, k):
        s = 0
        hashmap = {}
        res = 0
        
        for i,n in enumerate(nums):
            s += n
            if s == k:
                res += 1
            if s-k in hashmap:
                res += hashmap[s-k]
            if s not in hashmap:
                hashmap[s] = 1
            else:
                hashmap[s] += 1
        return res
   
solution = Solution()

nums = [1, 2, 3]
k = 3

res = solution.subarraySum(nums, k)
print(res)