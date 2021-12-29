class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        counter = 0;
        for i in range(1, len(nums)):
            if not(nums[i] > nums[i - 1]):
                diff = nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i] +  diff
                counter += diff

        
        return counter