class Solution:
    def reverseParentheses(self, s: str) -> str:
        startIndex = s.find(")")
        index = startIndex - 1
        target = ""
        while startIndex != -1:
            c = s[index]
            while c != "(":
                target = target + c
                index = index - 1
                c = s[index]

            if startIndex < len(s) - 1:
                s = s[0:index] + target + s[startIndex + 1:]
            else:
                s = s[0:index] + target 
                
            startIndex = s.find(")")
            index = startIndex - 1
            target = ""
            
        return s
   