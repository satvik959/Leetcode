class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        answer = []
        for i in range(len(nums)):
            if nums[i] == target:
                answer.append(i)
        return answer
        