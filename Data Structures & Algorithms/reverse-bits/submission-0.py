class Solution:
    def reverseBits(self, n: int) -> int:
        bStr = bin(n)[2:].zfill(32)
        rev = bStr[::-1]

        return int(rev, 2)