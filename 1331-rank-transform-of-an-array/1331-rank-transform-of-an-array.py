class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(set(arr))
        d = {}

        for i in range(len(a)):
            d[a[i]] = i + 1

        for i in range(len(arr)):
            arr[i] = d[arr[i]]

        return arr