class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = words[::-1]
        reversed_string = ' '.join(reversed_words)
        return reversed_string

# Example usage:
sol = Solution()
print(sol.reverseWords("the sky is blue"))        # Output: "blue is sky the"
print(sol.reverseWords("  hello world  "))        # Output: "world hello"
print(sol.reverseWords("a good   example"))       # Output: "example good a"