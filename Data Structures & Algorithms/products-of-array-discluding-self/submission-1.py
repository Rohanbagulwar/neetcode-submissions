class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # prefix
        prefix = [1]
        a=nums
        for i in range(len(a)):
            prefix.append(prefix[-1] * a[i])

        # postfix (built in reverse)
        postfix = [1]
        for j in range(len(a)-1, -1, -1):
            postfix.append(postfix[-1] * a[j])

        # combine
        result = []
        n = len(a)
        for i in range(n):
            result.append(prefix[i] * postfix[n - i - 1])

        return result
        