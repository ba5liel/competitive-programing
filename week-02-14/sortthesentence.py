class Solution:
    def sortSentence(self, s: str) -> str:
        sentences = s.split()
        
        numbers = list(map(self.mapToIndex, sentences))

        indexToSentence = numbers.copy()
      
        self.sort(numbers)
        
        newSentence = ""
        for i in range(len(numbers)):
            st = sentences[indexToSentence.index(numbers[i])][0:-1]
            if i == 0:
                newSentence = st
            else:
                newSentence = newSentence + " " + st

        return newSentence
    def mapToIndex(self, s: str) -> int:
        return int(s[len(s) - 1])
    
    def sort(self, arr: list):
        #insertion
        for i in range(1, len(arr)):
            temp = arr[i]
            for j in range(i - 1 ,-1, -1):
                if arr[j] > temp:
                    arr[j + 1] = arr[j]
                else:
                    arr[j + 1 ] = temp
                    break
            else:
                arr[0] = temp
            
        
 