"""
    question description:
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    Example:
        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
"""
class Solution(object):
    """
    输入一个数组列表和一个目标数，找出两个列表元素之和等于目标数的index(第一个索引)
    """
    def twosum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        generator_sum = ([indx1, indx2 + indx1+1] for indx1, value1 in enumerate(nums) 
                                                                 for indx2, value2 in enumerate(nums[indx1+1:]) if value1 + value2 == target)
        return next(generator_sum)
