class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        s = 0
        while (low <= high):
            c = 0
            mid = int((low + high) / 2)
            for pile in piles:
                c += int((pile + mid-1)/mid)
            if (c <= h):
                high = mid-1
                s = high
            else:
                low = mid+1
        return s+1

