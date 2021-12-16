class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count = count + 1
            res[i] = count
        return res