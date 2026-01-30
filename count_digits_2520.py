class Solution:
    def countDigits(self, num: int) -> int:
        original = num
        count = 0

        #int has no len so need to have workaround
        while num > 0:
            digit = num % 10

            #avoiding divi by 0
            #also checking if divisor completely
            #divides the number
            if digit != 0 and original % digit == 0:
                count += 1

            num //= 10

        return count

        