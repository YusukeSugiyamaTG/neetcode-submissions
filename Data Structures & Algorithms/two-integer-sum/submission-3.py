class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outputs = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in outputs:
                return [outputs[x], i]
            else:
                outputs[num] = i
        return []
        
                