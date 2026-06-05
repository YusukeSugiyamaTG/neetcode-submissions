class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outputs = []
        sorted_numbers = sorted(nums)

        for i, n in enumerate(sorted_numbers):
            # early return(if total will be 0, SHOULD include sorted_numbers[i] = `-x`)
            if n > 0:
                break
            # skip duplicate i(index)
            if i > 0 and sorted_numbers[i] == sorted_numbers[i-1]:
                continue

            # left should be index + 1
            left = i + 1
            right = len(sorted_numbers) - 1
            while left < right:
                total = n + sorted_numbers[left] + sorted_numbers[right]
                if total == 0:
                    outputs.append([n, sorted_numbers[left], sorted_numbers[right]])
                    left += 1
                    right -= 1
                    # skip duplicate left, right value
                    while left < right and sorted_numbers[left] == sorted_numbers[left - 1]:
                        left += 1
                    while left < right and sorted_numbers[right] == sorted_numbers[right + 1]:
                        right -= 1
                elif total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
        return outputs