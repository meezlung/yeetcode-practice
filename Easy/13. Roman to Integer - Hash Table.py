class Solution():
    def romanToInt(self, s):
        ans = 0
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        print(s)
        print(s[1:])
        tite = zip(s, s[1:])
        print(tuple(tite))

        for a, b in zip(s, s[1:]): # recursively identify each two pair all throughout the string
            if roman[a] < roman[b]:
                ans -= roman[a]
            else:
                ans += roman[a]
            
        return ans + roman[s[-1]] 
        # just dont forget to add the value of the last one 
        # because it's not included in the zip

        
solution = Solution()
print(solution.romanToInt("III")) # => 3
print(solution.romanToInt("LVIII")) # => 58
print(solution.romanToInt("MCMXCIV")) # => 1994