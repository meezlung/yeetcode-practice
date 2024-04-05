class Solution(object):
    def encode(self, strs: list[str]) -> str:
        placeholder = ["#"]
        for str in strs:
            placeholder.append(str)
            placeholder.append("#")
        
        return "".join(placeholder)

    def decode(self, str: str) -> list[str]:
        if str == "##":
            return [""]

        original_word = []
        word = []

        for letter in str:
            if letter != "#":
                word.append(letter)
            else:
                if word:
                    original_word.append("".join(word))
                    word = []
        
        return original_word


solution = Solution()
print(solution.encode(["neet","code","love","you"]))
print(solution.decode("#neet#code#love#you#"))
print(solution.encode([""]))
print(solution.decode("##"))
print(solution.encode(["a"]))
print(solution.decode("#a#"))

