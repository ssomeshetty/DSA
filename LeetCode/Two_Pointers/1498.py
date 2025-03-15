# 1498. Number of Subsequences That Satisfy the Given Sum Condition


# Example 1:

# Input: nums = [3,5,6,7], target = 9
# Output: 4
# Explanation: There are 4 subsequences that satisfy the condition.
# [3] -> Min value + max value <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)
# Example 2:

# Input: nums = [3,3,6,8], target = 10
# Output: 6
# Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
# [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
# Example 3:

# Input: nums = [2,3,3,4,6,7], target = 12
# Output: 61
# Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
# Number of valid subsequences (63 - 2 = 61).


from itertools import combinations

class Solution(object):
    def numSubseq(self, nums, target):
        nums.sort()
        res = 0
        mod = 10**9+7
        l,r = 0,len(nums)-1

        while l<=r:
            if nums[l] + nums[r] <= target :
                res += 2**(r-l)
                res = res % mod
                l+=1
            else:
                r-=1
        return res

class Solution(object):
    def numSubseq(self, nums, target):
        res = 0
        for i in range(1,len(nums)+1): # this is using for counting purpose 1-> len(nums) this is not indexing
            for j in combinations(nums,i):
                min_ = min(j)
                max_ = max(j)
                if min_ + max_ <= target:
                    res += 1
        return res


        