class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        self.mergeInterval(intervals, 0)
        return intervals
    
    def mergeInterval(self, arr , j):
        iLength = len(arr)
        print(f"INTERVAL LIst {arr}")
        print(f"CURRENT INTERVAL CHECKING FIRST - {arr[j]}")
        for i in range(j + 1, iLength):
            print(f"CURRENT INTERVAL CHECKING SECOND - {arr[i]}")
            if self.haveIntersection(arr[j], arr[i]):
                    arr[j] = [min(arr[j][0], arr[i][0]),  max(arr[j][1], arr[i][1])]
                    arr.pop(i)
                    print(f"IS IN RANGE new INTERVAL becomes - {arr}")
                    break
        if iLength == len(arr):
            if j < len(arr):
                self.mergeInterval(arr, j + 1)
        else:
            if j < len(arr) - 1:
                self.mergeInterval(arr, 0)
        
    
    def haveIntersection(self, interval1, interval2) -> bool:
        
        return interval2[0] <= interval1[1] and interval2[1] >= interval1[0]