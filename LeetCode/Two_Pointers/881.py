# 881. Boats to Save People

# Example 1:

# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# Example 2:

# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# Example 3:

# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
 


class Solution(object):
    def numRescueBoats(self, nums, limit):
        res = 0
        nums.sort()
        l,r = 0,len(nums)-1
        while l<=r:
            if nums[l] + nums[r] <= limit:
                res += 1
                l+=1
                r-=1
            else:
                res += 1
                r-=1
        return res
    
solution = Solution()

print(solution.numRescueBoats([1,3,4,2,5],5))




                    

        