"""Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint."""

from math import inf
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        sum_list = 0
        # minimum target sum
        min_mts = inf

        for r in range(len(nums)):
            sum_list += nums[r]

            while(sum_list >= target):
                mts = r - l + 1
                min_mts = min(mts, min_mts)
                sum_list -= nums[l]
                l += 1
        
        if(min_mts == inf):
            return 0
        else: 
            return min_mts      
        
if __name__ == "__main__":
    sol = Solution()

    tests = [
        # (target, nums, expected)
        (7, [2,3,1,2,4,3], 2),        # [4,3] is the shortest
        (4, [1,4,4], 1),              # [4]
        (11, [1,1,1,1,1,1,1,1], 0),   # no subarray reaches target
        (15, [5,1,3,5,10,7,4,9,2,8], 2),  # [8,7] or [7,8]
        (3, [1,1,1,1,1], 3),          # [1,1,1]
        (11, [1,2,3,4,5], 3),         # [3,4,5]
    ]

    for target, nums, expected in tests:
        result = sol.minSubArrayLen(target, nums)
        print(f"target={target}, nums={nums}")
        print(f"Output: {result} | Expected: {expected}")
        print('-' * 40)
