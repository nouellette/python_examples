class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result

sol = Solution()
print(sol.singleNumber([2, 2, 1]))        # Output: 1
print(sol.singleNumber([4, 1, 2, 1, 2]))  # Output: 4
print(sol.singleNumber([1]))              # Output: 1
print(sol.singleNumber([5, 9]))           # Output: 12 wrong!