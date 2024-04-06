# class Solution(object):
#     def encode(self, strs: list[str]):
#         encoded = ""
#         for s in strs:
#             encoded += "#" + str(len(s)) + s

#         return encoded

#     def decode(self, str: str):
#         decoded = []
#         i = 0

#         while i < len(str):
#             word = []
#             length = 0
#             if str[i] == "#":
#                 length = int(str[i + 1])

#                 for j in range(i + 2, i + length + 2):
#                     word.append(str[j])

#             decoded.append(''.join(word)) 
#             i += 2 + length
#         return decoded

class Solution:
    
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            print('i', j)
            print('j', j)

            print(s[i:j])
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res 

solution = Solution()
# print(solution.encode(["neet","code","love","you"]))
# print(solution.decode("#4neet#4code#4love#3you"))
# print(solution.encode([""]))
# print(solution.decode("#0"))
# print(solution.encode(["a"]))
# print(solution.decode("#1a"))
print(solution.encode(["we","say",":","yes","!@#$%^&*()"]))
print(solution.decode("2#we3#say1#:3#yes10#!@#$%^&*()"))

