class Solution(object):
    def divideNumbers(self, numbers, target, filtered_list=[]):
        n = len(numbers)

        if n % 2 == 0:
            mid = n // 2
            if numbers[mid]:
                pass

    def twoSum(self, numbers, target):
        self.divideNumbers(numbers, target)

        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                if numbers[i] + numbers[j] == target and i != j:
                    return [i + 1, j + 1]

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([2,3,4], 6))
print(solution.twoSum([-1,0], -1))
print(solution.twoSum([0, 0, 3, 4], 0))

