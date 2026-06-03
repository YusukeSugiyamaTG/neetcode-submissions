class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        charSet = set()
        for num in nums:
            if num in charSet:
                return True
            charSet.add(num)
        return False