import time

class Solution(object):
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
    
    def main(self):
        start_time = time.time()
        self.strStr("butsadsad", "sad")
        end_time = time.time()

        return (end_time - start_time) * 1000

solution = Solution()
# print(solution.strStr("butsadsad", "sad"))
# print(solution.strStr("leetcode", "leeto"))        
print(solution.main())