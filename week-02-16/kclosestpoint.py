class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = {}
        distanceArr = []
        
        for i in range(len(points)):
            d = points[i][0]**2 + points[i][1]**2
            distanceArr.append(d)
            distance[f'{d}'] = points[i]
        self.sorti(distanceArr)
        
        answer = []
        for i in range(k):
            answer.append(distance[f'{distanceArr[i]}'])
        
        return answer
       
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