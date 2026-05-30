class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        outputs = []

        for i, num in enumerate(sorted_nums):
            if num > 0:
                break
            # 重複スキップ
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            # リストから取得した数字をゼロから減算する
            target = 0 - num
            left = i + 1
            right = len(sorted_nums) - 1
            while left < right:
                if sorted_nums[left] + sorted_nums[right] == target:
                    outputs.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    # 重複スキップ
                    while left < right and sorted_nums[left] == sorted_nums[left-1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right+1]:
                        right -= 1
                elif sorted_nums[left] + sorted_nums[right] > target:
                    right -= 1
                elif sorted_nums[left] + sorted_nums[right] < target:
                    left += 1
        # if NOT sum up to 0
        return outputs
