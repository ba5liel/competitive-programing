def isort(arr: list[int]):
        #insertion
        for i in range(1, len(arr)):
            current = arr[i]
            for j in range(i - 1, -1, -1):
                if arr[j] > current:
                    arr[j+1] = arr[j]
                    arr[j] = current
                else:
                    arr[j+1] = current
                    break

isort([5,2,4,3,1])