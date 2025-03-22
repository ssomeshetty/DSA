# 917. Reverse Only Letters

# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

 

# Example 1:

# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

class Solution(object):
    def reverseOnlyLetters(self, s):
        nums = list(s)
        l,r = 0,len(nums)-1
        while l<r:
            if not nums[l].isalpha():    #isalpha() -> aphlabetic only , isalnum() includes alpabets,numbers also
                l+=1
            elif not nums[r].isalpha():
                r-=1
            else:
                nums[l] , nums[r] = nums[r],nums[l]
                l+=1
                r-=1
        return ''.join(nums)
        