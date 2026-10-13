class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for ch in s:
            if ch in opening:                
                stack.append(ch)
            else:                            
                if not stack:                
                    return False
                if opening[stack.pop()] != ch:
                    return False

        return len(stack) == 0

        

        
        