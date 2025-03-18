# 680. Valid Palindrome II

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# 467 / 474 testcases passed
class Solution(object):
    def validPalindrome(self, nums):
        i,j = 0,len(nums)-1
        cnt = 0
        while i<=j:
            if nums[i] == nums[j] :
                i+=1
                j-=1
            else:
                if i+1 <=j and nums[i+1] == nums[j]:
                    cnt += 1
                    i+=1
                elif nums[j-1] == nums[i]:
                    cnt+=1
                    j -= 1
                else:
                    return False

        return True if cnt <= 1 else False
        
class Solution(object):
    def validPalindrome(self, s):
        if s == s[::-1]:
            return True
        
        l, r =0, len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                temp2 = s[:r] + s[r+1:]
                temp = s[:l] + s[l+1:]
                
                return temp == temp[::-1] or temp2 == temp2[::-1]
            
            l +=1
            r -=1

