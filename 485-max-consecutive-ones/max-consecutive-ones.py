class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        temp = 0
        for i in range(len(nums)):
            if (nums[i] == 1):
                temp += 1
                print(temp)
                longest = max(longest,temp)
            else:
                longest = max(longest,temp)
                temp = 0
        return longest
            