class Solution(object):
    def isSubsequence(self, s, t):
        charFound = []

        for c in t:
            if c in s:
                charFound.append(c)
        orderedResult = ''.join(charFound)

        return s in orderedResult

s = Solution()
print(s.isSubsequence('abc', 'ahbgdc')) # True