class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        for i, num in enumerate(nums):
            nums[i] = int(num)
        
        nums = sorted(nums, reverse=True)
        return str(nums[k - 1])