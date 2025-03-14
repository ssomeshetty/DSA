# 525. Contiguous Array


# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Example 3:

# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.

# Brute Force
class Solution(object):
    def __init__(self,nums):
        self.nums = nums
        
    def findMaxLength(self):
        res = 0
        for i in range(len(self.nums)):
            cnt0 = cnt1 = 0
            for j in range(i,len(self.nums)):
                if self.nums[j] == 0:
                    cnt0 += 1
                else:
                    cnt1 += 1
                if cnt0 == cnt1 :
                    res = max(res,cnt0 + cnt1)
        return res

s = Solution([1,1,0 ,0 , 0,1, 0])
res = s.findMaxLength()
print(res)


# Optimal Approach best approach

class Solution(object):
    def findMaxLength(self, nums):
        cnt0 = cnt1 = 0
        res = 0
        hashmap = {}   # cnt1 - cnt0 --> i
        for i,n in enumerate(nums):
            if n == 0:
                cnt0 += 1
            else:
                cnt1 += 1

            if cnt1 - cnt0 not in hashmap:
                hashmap[cnt1-cnt0] = i
            
            if cnt1 == cnt0:
                res = cnt1 + cnt0
            if cnt1 - cnt0 in hashmap:
                idx = hashmap[cnt1-cnt0]
                res = max(res,i-idx)
        return res
    

# my approach  280 / 565 test cases
class Solution(object):
    def findMaxLength(self, nums):
        cnt1 = 0
        cnt0 = 0
        value = 0
        max_ = 0
        cnt = 0
        for i in range(len(nums)):
            if cnt1 == 0 and cnt0 == 0:
                if nums[i] == 0:
                    cnt0 = 1
                if nums[i] == 1:
                    cnt1 = 1
            else:
                if cnt1 > 0:
                    if nums[i] == 1 and nums[i-1] == 1:
                        cnt1 += 1
                        value = max(value , cnt1)
                    else:
                        cnt1 -= 1
                        max_ = max(max_ , value - cnt1)
                        if max_ == 0:
                            cnt += 1
                if cnt0 > 0:
                    if nums[i] == 0 and nums[i-1] == 0:
                        cnt0 += 1
                        value = max(value , cnt0)
                    else:
                        cnt0 -= 1
                        max_ = max(max_ , value - cnt0)
                        if max_ == 0:
                            cnt += 1
        return max_ * 2 if max_ > 0 else cnt * 2
    

