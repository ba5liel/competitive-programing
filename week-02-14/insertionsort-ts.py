def isort(self, arr: List[int]):
        #insertion
        for i in range(1, len(arr)):
            current = arr[i]
            for j in len(i, -1, -1):
                if arr[j] > current:
                    arr[i] = arr[j]
                    if j == 0:
                        arr[j] = current
                elif:
                    arr[i] = current
                    break