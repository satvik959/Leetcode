class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = strs[0]

        for s in strs:
            while not s.startswith(a):
                a = a[:-1]

        return a