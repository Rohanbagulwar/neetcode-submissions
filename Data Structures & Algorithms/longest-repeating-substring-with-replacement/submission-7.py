class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        final_ans=0
        for i in range(len(s)):
            for target in set(s):
                temp_ans=''
                count2=0
            # temp_ans+=s[i]/
                for j in range(i,len(s)):
                    if s[j] != target:
                        if count2 == k:
                            break
                        count2 += 1
            
                    temp_ans += s[j]



                final_ans=max((final_ans),len(temp_ans))
        return final_ans
        