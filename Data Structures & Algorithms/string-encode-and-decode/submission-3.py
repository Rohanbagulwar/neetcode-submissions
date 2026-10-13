class Solution:

    def encode(self, strs: List[str]) -> str:
        a=''
        for i in strs:
            a+=i
            a+='~'
        return a


    def decode(self, s: str) -> List[str]:
        return s.split('~')[:-1]
