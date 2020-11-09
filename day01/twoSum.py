#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : WGQ
# @Time    : 2020/11/9 19:11

from typing import List

'''
给定一个整数数组nums和一个目标值target，
请你在该数组中找出和为目标值的那两个整数，
并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。
但是数组中的一个元素不能使用两遍。
'''
'''
示例：
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

class Solution1:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1,n):
                if nums[i] + nums[j] == target:
                    return [i, j ]
        return []

class Solution2:
    '''
    时间复杂度从O(N)降低到O(1)
    创建哈希表，对于每一个 x ，
    首先查询哈希表中是否存在 target - x，
    然后将x插入到哈希表中，即可保证不会让x和自己匹配到
    '''
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i,num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


if __name__ == '__main__':

    nums = [2, 7, 11, 15]
    target =9
    solute1 = Solution1()
    solute2 = Solution2()
    print(solute1.twoSum1(nums = nums, target = target))
    print(solute2.twoSum2(nums = nums, target = target))