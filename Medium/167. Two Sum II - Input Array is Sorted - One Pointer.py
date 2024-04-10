class Solution(object):
    def twoSum(self, numbers, target):
        pointer = len(numbers) - 1

        for i, num in enumerate(numbers):
            while pointer > i and numbers[pointer] > target - num:
                pointer -= 1

            if numbers[pointer] == target - num:
                return [i + 1, pointer + 1]



solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([2,3,4], 6))
print(solution.twoSum([-1,0], -1))
print(solution.twoSum([0, 0, 3, 4], 0))

