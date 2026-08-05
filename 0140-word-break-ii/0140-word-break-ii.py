class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            res = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in wordSet:
                    for sub in dfs(end):
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)

            memo[start] = res
            return res

        return dfs(0)