from bisect import bisect_left # this is for second function

class Solution(object):
    def lengthOfLIS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
    
    def lengthOfLIS(self, nums):
        tails = []

        for num in nums:
            if not tails or num > tails[-1]:
                tails.append(num)

            else:
                tails[bisect_left(tails, num)] = num

        print(tails)
        return len(tails)

solution = Solution()
print(solution.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(solution.lengthOfLIS([0,1,0,3,2,3]))
print(solution.lengthOfLIS([7,7,7,7,7,7,7]))