class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []

        for c in num:
            print('C', c)
            while k > 0 and stack and stack[-1] > c:
                # if new c is lesser than current c in the last
                # stack, then pop the current sht then append the
                # new c
                k -= 1
                stack.pop()
                print('Stack', stack)
            
            stack.append(c)
            print('Stack', stack)

        stack = stack[:len(stack) - k]
        return str(int(''.join(stack))) if stack else "0"
        
solution = Solution()
print(solution.removeKdigits("1432219", 3))
print(solution.removeKdigits("10200", 1))
print(solution.removeKdigits("10",2))
print(solution.removeKdigits("10001", 4))
print(solution.removeKdigits("10001", 3))