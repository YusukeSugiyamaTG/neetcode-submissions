class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            diff = target - numbers[left]
            if diff == numbers[right]:
                return [left + 1, right + 1]
            elif diff < numbers[right]:
                right -= 1
            elif diff > numbers[left]:
                left += 1
        return []