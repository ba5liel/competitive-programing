class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        answer = []
        minV = int(len(nums)/3)
        for n in nums:
            if n in freq:
                freq[n] = freq[n] + 1
            else:
                freq[n] = 1
                
        
        for key, value in freq.items():
            if value > minV:
                answer.append(key)
                
        return answer