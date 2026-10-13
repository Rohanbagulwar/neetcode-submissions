class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sol=[]
        for number in range(len(numbers)):
            for pt2 in range(number+1,len(numbers)):
                
                if numbers[pt2]==target-numbers[number]:
                    sol.append(number+1)
                    sol.append(pt2+1)
                    return sol