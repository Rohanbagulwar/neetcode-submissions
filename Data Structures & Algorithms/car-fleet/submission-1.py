class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_ls = list(zip(position, speed))
        ls2 = []

        new_ls.sort(key=lambda x: x[0], reverse=True)
        count = 0

        for i, j in new_ls:
            ans = (target - i) / j
            if count != 0:
                if ls2[-1] > ans:
                    pass
                else:
                    ls2.append(ans)
            else:
                ls2.append(ans)
            count += 1
        return len(set(ls2))
                