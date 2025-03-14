# 303. Range Sum Query - Immutable

# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3


class NumArray(object):

    def __init__(self, nums):
        self.prefix_sum = []
        sum_at_step = 0
        for n in nums:
            sum_at_step += n
            self.prefix_sum.append(sum_at_step)
    def sumRange(self, left, right):
        right_value = self.prefix_sum[right]
        left_value = self.prefix_sum[left-1] if left > 0 else 0

        return right_value - left_value
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)