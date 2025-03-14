# 15. 3Sum

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.


class Solution(object):
    def threeSum(self, nums):
        num = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i >= 1:
                continue
            j = i+1
            k = len(nums) - 1
            while j < k:
                value = nums[i] + nums[j] + nums[k]
                if value == 0:
                    num.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
                elif value > 0:
                    k-=1
                else:
                    j+=1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
        return num
    

class Solution(object):
    def threeSum(self, nums):
        num = set()
        nums.sort()

        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1
            while j < k:
                value = nums[i] + nums[j] + nums[k]
                if value == 0:
                    num.add(tuple(sorted([nums[i],nums[j],nums[k]])))
                    j+=1
                elif value > 0:
                    k-=1
                else:
                    j+=1
        return list(num)

class Solution(object):
    def threeSum(self, nums):
        hashmap = {}

        for i,n in enumerate(nums):
            hashmap[n] = i
        num = set()

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                value = 0 - nums[i] - nums[j] 
                if value in hashmap and hashmap[value] != i and hashmap[value] != j:
                    num.add(tuple(sorted([nums[i],nums[j],value])))
        return list(num)
    
    
class Solution(object):
    def threeSum(self, nums):
        num = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        num1 = (sorted([nums[i],nums[j],nums[k]]))
                        if num1 not in num:
                            num.append(num1)
        return num
                





        
        