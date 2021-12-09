class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer:List[str] = []
        for i in range(n):
            index: int = i+1;
            currentValue: str = f'{index}';
            if index % 3 == 0 and index % 5 == 0:
                currentValue = "FizzBuzz"
            elif index % 3 == 0:
                currentValue = "Fizz"
            elif index % 5 == 0:
                currentValue = "Buzz"
                
            answer.append(currentValue)
        return answer
            