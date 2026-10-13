class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        a=nums
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                for k in range(j+1,len(a)):
                    if a[i]+a[j]+a[k]==0:

                        temp_ls=sorted([a[i],a[j],a[k]])
                        if temp_ls not in ans:
                            ans.append(temp_ls)

        return ans
        