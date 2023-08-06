class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        lookup={")":"(","}":"{","]":"["}
        for p in s:
            if p in lookup.values():
                stack.append(p)
                
            elif stack and lookup[p]==stack[-1]:
                stack.pop()
                
            else:
                return False
        return stack==[]
class Solution:
    def isValid(self,s:str)->bool:
        brackets=['()','{}','[]']
        while any(x in s for x in brackets):
            for br in brackets:
                s=s.replace(br,'')

        return not s  

class Solution:
    def isValid(self,s:str)->bool:
        return s=='' if s==(s:=s.replace('()','').replace('{}','').replace('[]','')) else self.isValid(s)               
