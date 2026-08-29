class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # r = 11
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for banana in piles:
                hours += math.ceil(banana / k) # 6
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res





# what i learned:
    # since we can only choose one pile for an hour, h must >= the len of piles
        