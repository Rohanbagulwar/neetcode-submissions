class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        low,high=1,max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            # print(i)
            temp_hours=0
            for j in piles:
                temp_hours+=math.ceil(j/mid)

            if temp_hours<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        
        return ans


        