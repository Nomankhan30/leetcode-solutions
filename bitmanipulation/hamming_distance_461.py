#hamming distance is the number of bits which are different in two integers 
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #removing first 2 indices 0b
        bv = bin(x)[2:]
        bv1 = bin(y)[2:]
        count = 0
        #making both integers of same length in terms of bits
        if len(bv) < len(bv1):
            #We need to match bigger binary number length 
            #and we always pick bit of bigger number in order 
            #to make a specific binary number so 0s should be added from the start 
            #not from the end.
            while len(bv) < len(bv1):
                bv = '0' + bv
        else:
            while len(bv1) < len(bv):
                bv1 = '0' + bv1

        for index in range(len(bv)):
            #if xor produces 1 it means at this position, bits are different for both integers
            #so we will increment the count of number of different bits
            if int(bv[index]) ^ int(bv1[index]) == 1:
                count += 1

        return count
