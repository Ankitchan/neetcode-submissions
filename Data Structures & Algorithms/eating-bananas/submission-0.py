class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #totSum = 0
        #for i in range(len(piles)):
        #    totSum = totSum + piles[i]
        
        left = 1
        right = max(piles)
        #right = totSum
        while(left < right):
            mid = (right + left) // 2
            #mid = (right - left) // 2 + 1
            # can eat all bananas in h hours
            totTime = 0

            for j in range(len(piles)):
                totTime += math.ceil(piles[j] / mid)
            
            #print("totTime: " + str(totTime))
            if totTime > h:
                left = mid + 1
            else:
                right = mid
                
        
        return left