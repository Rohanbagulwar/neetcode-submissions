class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        count_t = Counter(t)

        ans = ""

        for i in range(len(s)):
            temp_str = ""

            for j in range(i, len(s)):
                temp_str += s[j]

               
                new_dict = dict.fromkeys(count_t.keys(), 0)

              
                for k in temp_str:
                    if k in new_dict:
                        new_dict[k] += 1

         
                valid = True
                for ch in count_t:
                    if new_dict[ch] < count_t[ch]:
                        valid = False
                        break

                if valid:
                    if ans == "" or len(temp_str) < len(ans):
                        ans = temp_str
                    break 
        return ans  
            
        