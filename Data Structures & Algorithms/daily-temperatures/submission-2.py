class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a=temperatures
        res=[]
        for i in range(0,len(a)):
            count=0

            first_count=False
            found=False
            for j in range(i+1,len(a)):

                count+=1
                if a[i]<a[j]:
                    res.append(count)
                    found=True
                    break
            if not found:
                res.append(0)
        return res

        