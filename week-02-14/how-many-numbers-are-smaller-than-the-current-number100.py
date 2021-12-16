class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101
        res = [None] * len(nums)
        for i in range(len(nums)):
            count[nums[i]] = count[nums[i]] + 1
            
        for i in range(1, len(count)):
            count[i] = count[i] + count[i - 1]

        for i in range(len(nums)):
            if nums[i] == 0:
                res[i] = 0
            else:
                res[i] = count[nums[i] - 1]

        return res