class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = {}
        for i, n in enumerate(nums):
            rest = target - n
            if rest in out:
                return [out[rest], i]
            else:
                out[n] = i
        return []