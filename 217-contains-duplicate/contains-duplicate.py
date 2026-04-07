class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = nums[i]
        if (len(seen) < len(nums)):
            return True
        return False
            