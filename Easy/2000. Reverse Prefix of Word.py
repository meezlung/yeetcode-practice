class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        answer = ''

        for idx in range(len(word)):
            if word[idx] == ch:
                answer = word[:idx+1][::-1] + word[idx+1:]
                break

        return answer if answer else word
    
solution = Solution()
print(solution.reversePrefix("abcdefd", "d"))
print(solution.reversePrefix("xyxzxe", "z"))
print(solution.reversePrefix("abcd", "z"))