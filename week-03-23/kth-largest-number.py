class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        divisions = {}
        for s in nums:
            if len(s) in divisions:
                divisions[len(s)].append(s)
            else:
                divisions[len(s)] = [s]

        targetList = []
    

        divisionsList = list(dict(sorted(divisions.items(), reverse=True)).values())

        for d in divisionsList:
            if len(d) >= k:
                targetList = d
                break
            else:
                k = k - len(d)
        
        for i in range(1, len(targetList)):
            for j in range(i - 1, -1, -1):
                if int(targetList[j + 1]) > int(targetList[j]):
                    targetList[j], targetList[j + 1] = targetList[j + 1], targetList[j]
                else:
                    break;
    
        return targetList[k - 1]