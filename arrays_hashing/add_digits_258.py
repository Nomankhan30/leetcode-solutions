class Solution:
    def addDigits(self, num: int) -> int:
        #using most basic approach otherwise it can
        #done using modulo as well
        while num >= 10:
            sum_ = 0
            while num > 0:
                sum_ += num % 10  #add last digit
                num //= 10         #remove last digit
            num = sum_
        return num
