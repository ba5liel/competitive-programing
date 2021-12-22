class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newResult = [intervals[0]]
        
        for i in range(1, len(intervals)):
            openU = intervals[i][0]
            closeU = intervals[i][1]
            print(f"new result[] current satate: {newResult}")
            print(f"current inverval {intervals[i]}")
            for j in range(len(newResult)):
                result = newResult[j]
                print(f"checking result {result}")
                isInbound = openU <= result[1] and closeU >= result[0]
                print(f"isInBound {isInbound}")    
                if isInbound:
                    result[0] = min(openU, result[0])
                    result[1] = max(closeU, result[1])
                    print(f"new result value {result}")
                    break

                else:
                    if j == len(newResult) - 1:
                       newResult.append([openU, closeU])
                       print(f"new result value not bound {[openU, closeU]}")
                    
            
        return newResult
                
            