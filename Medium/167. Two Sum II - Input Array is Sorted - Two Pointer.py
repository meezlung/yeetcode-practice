class Solution(object):
    def twoSum(self, numbers, target):
        start, end = 0, len(numbers) - 1

        while start != end:
            if numbers[start] + numbers[end] > target:
                end -= 1

            elif numbers[start] + numbers[end] < target:
                start += 1

            else:
                return [start + 1, end + 1]            


solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([2,3,4], 6))
print(solution.twoSum([-1,0], -1))
print(solution.twoSum([0, 0, 3, 4], 0))

