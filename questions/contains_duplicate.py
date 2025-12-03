"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""
def contain_duplicate(nums):
    test_set = set(nums)

    if len(nums) == len(test_set):
        # no duplicate
        return False
    else:
        # duplicate
        return True    


test = [1, 2, 3, 4]
print(contain_duplicate(test))
