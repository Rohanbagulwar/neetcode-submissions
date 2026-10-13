class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<k:
            return []
        j=0
        ls=[]
        for i in range(len(nums)-k+1):
            if i==0:
                j+=k
                ls.append(max(nums[i:j]))
            else:
                j+=1
                ls.append(max(nums[i:j]))
                
        return ls
        