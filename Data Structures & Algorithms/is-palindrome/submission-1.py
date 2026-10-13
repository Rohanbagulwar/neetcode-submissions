class Solution:
    def check_alphanumeric(self,char: str) -> bool:

        if (65<=ord(char)<=90) or (97<=ord(char)<=122) or (47<=ord(char)<=57):
            return True
        else:
            return False
    def isPalindrome(self, s: str) -> bool:
        start=0
        end=len(s)
        clean_string=''
        reverse_string=''
        for i in s:
            if self.check_alphanumeric(i):
                clean_string+=i.lower()

        for j in range(len(clean_string)-1,-1,-1):
            reverse_string+=clean_string[j]
        
        if reverse_string==clean_string:
            return True
        else:
            return False