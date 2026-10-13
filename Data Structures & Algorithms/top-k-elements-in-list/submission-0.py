class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        count=0
        ls=[]
        for i in nums:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1

        a=sorted(a.items(),key=lambda k:k[1],reverse=True)
        print(a)
        for i in a:
            if count==k:
                break
            else:
                # pass
                ls.append(i[0])
        
            count+=1
        return ls
        