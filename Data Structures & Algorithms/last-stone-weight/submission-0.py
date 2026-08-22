class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()

        print(list(stones))

        while len(stones) > 1:
            if stones[len(stones)-1] == stones[len(stones)-2]:
                stones.pop()
                stones.pop()
            else:
                stones[len(stones)-2] = stones[len(stones)-1] - stones[len(stones)-2]
                stones.pop()
                stones.sort()
        
        if len(stones) == 1:
            return stones[0]
        else:
            return 0