# 345. Reverse Vowels of a String


# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

class Solution(object):
    def reverseVowels(self, s):
        nums = list(s)
        l,r = 0,len(nums)-1
        vowels = "AEIOUaeiou"
        while l<=r:
            if nums[l] not in vowels:
                l+=1
            elif nums[r] not in vowels:
                r-=1
            else:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1
                    
        return ''.join(nums)