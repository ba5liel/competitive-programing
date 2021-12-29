class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxX = 1
        
        for i in range(len(nums) - 1, 0, -1):
            diff = k
            maxY = 1
            for j in range(i - 1, -1, -1):
                diff = diff - (nums[i] - nums[j])
                if diff < 0:
                    break
                maxY += 1
            maxX = max(maxX, maxY)
        
        return maxX
            
            