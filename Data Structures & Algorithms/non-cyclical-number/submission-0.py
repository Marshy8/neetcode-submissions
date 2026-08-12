class Solution:
    def isHappy(self, n: int) -> bool:
        digits = [int(d) * int(d) for d in str(n)]
        
        seen = {}

        seen[sum(digits)] = sum(digits)

        print(seen)

        while seen[sum(digits)] != 1:
            
            digits = [int(d) * int(d) for d in str(sum(digits))]
            if sum(digits) in seen:
                return False
            seen[sum(digits)] = sum(digits)
            
            

        return True
