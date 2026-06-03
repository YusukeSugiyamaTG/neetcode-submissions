class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outputs = {}
        for i, num in enumerate(nums):
            rest = target - num
            if rest in outputs:
                return [outputs[rest], i]
            else:
                outputs[num] = i
        return []