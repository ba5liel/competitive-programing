class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        newResult = []
        for i in range(1, len(intervals)):
        
            if  intervals[i-1][1] >= intervals[i][0]:
                newResult.append([intervals[i-1][0], intervals[i][1]])
                intervals[i] = [intervals[i-1][0], intervals[i][1]]
            else:
                newResult.append(intervals[i])
        
        return newResult
                
            