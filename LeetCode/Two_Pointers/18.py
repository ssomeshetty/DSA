# 18. 4Sum


# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]


class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        num = []
        i,j,k,l = 0,0,0,len(nums)-1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] :
                continue
            for j in range(i+1,len(nums)):
                if j > i+1 and nums[j] == nums[j-1] :
                    continue
                k = j+1
                l = len(nums)-1
                while k < l:
                    value = nums[i] + nums[j] + nums[l] + nums[k]
                    if value == target:
                        num.append([nums[i],nums[j],nums[k],nums[l]])
                        while k < l and nums[k] == nums[k+1]:
                            k+=1
                        k += 1
                    elif value < target:
                        k += 1
                    else:
                        l -= 1
        return num 
    


        ans = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    for l in range(k+1,len(nums)):
                        Sum = nums[i] + nums[j] + nums[k] + nums[l]
                        if Sum == target:
                            arr = tuple(sorted([nums[i],nums[j],nums[k],nums[l]]))
                            ans.add(arr)

        return list(ans)

        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    value = target - (nums[i] + nums[j] + nums[k])
                    if value in hashMap and hashMap[value] > k:
                        triplet = tuple(sorted([nums[i],nums[j],nums[k],value]))
                        ans.add(triplet)
        return list(ans)