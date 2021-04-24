"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
https://leetcode.com/problems/running-sum-of-1d-array/
"""

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = nums.split(',')
        res = list()
        res.append(int(num[0]))
        for i in range(1, len(num)):
            res.append(res[i - 1] + int(num[i]))
        return res


if __name__ == '__main__':
    test_inp = input()
    result = Solution()
    print(result.runningSum(test_inp))
