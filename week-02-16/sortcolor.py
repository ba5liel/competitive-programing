class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.sorti(nums)
        
    def sorti(self, arr):
        for i in range(1, len(arr)):
            current = arr[i]
            for j in range(i - 1, -1, -1):
                if arr[j] > current:
                    arr[j+1] = arr[j]
                    arr[j] = current
                else:
                    arr[j+1] = current
                    break
        
        