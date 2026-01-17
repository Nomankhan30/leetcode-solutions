class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            #Extract the i-th bit
            bit = (n >> i) & 1
            #Place it in the reversed position
            result |= bit << (31 - i)
        return result
