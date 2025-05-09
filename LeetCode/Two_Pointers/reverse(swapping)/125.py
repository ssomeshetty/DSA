# 125. Valid Palindrome

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

class Solution(object):
    def isPalindrome(self, nums):
        # s = ''.join(e for e in s if e.isalnum()).lower()
        # return s == s[::-1]


        i,j = 0,len(nums)-1
        while i<=j:
            if not nums[i].isalnum():
                i+=1
            elif not nums[j].isalnum():
                j-=1
            else:
                if nums[i].lower() == nums[j].lower():
                    i+=1
                    j-=1
                else:
                    return False
        return True
        

