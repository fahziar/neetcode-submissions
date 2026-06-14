class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) >= 2 :
            stoneA = heapq.heappop_max(stones)
            stoneB = heapq.heappop_max(stones)

            if stoneA > stoneB :
                stoneA = stoneA - stoneB
                heapq.heappush_max(stones, stoneA)
            elif stoneB > stoneA :
                stoneB = stoneB - stoneA
                heapq.heappush_max(stones, stoneB)

        if len(stones) == 0 :
            return 0
        else :
            return stones[0]
        