class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(self.mapToString, nums))
        
        for i in range(1, len(nums)):
            print(f"i {i}")
            
            for j in range(0, -1, -1):
                print(f"\nnew value {nums}")
                print(f"j {j}")
                print(f"j {nums[j]} j + 1 {nums[j + 1]}")
                for k in range(max(len(nums[j + 1]),len(nums[j]))):
                    
                    print(f"nums[j + 1][{k}] {nums[j + 1][min(k, len(nums[j + 1]) - 1)]}")
                    print(f"nums[j][{k}] {nums[j][min(k, len(nums[j]) - 1)]}")
                    if int(nums[j + 1][min(k, len(nums[j + 1]) - 1)]) > int(nums[j][min(k, len(nums[j]) - 1)]):
                        
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]   
                        break
                    elif int(nums[j + 1][min(k, len(nums[j + 1]) - 1)]) < int(nums[j][min(k, len(nums[j]) - 1)]):
                        
                        break
                    
        return "".join(nums)             
                    
                
                
    def mapToString(self, element):
        return str(element)