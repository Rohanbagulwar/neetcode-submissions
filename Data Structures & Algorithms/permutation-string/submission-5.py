class Solution:

    def checkInclusion(self,s1:str, s2:str)->bool:
        n = len(s1)
        
        if n > len(s2):
            return False

        for i in range(len(s2) - n + 1):
            sub = s2[i:i+n]      # take substring of same length
            if sorted(sub) == sorted(s1):
                return True

        return False