def armstrong(n):
    num = n
    sum_of_powers = 0
    
    while num > 0:
        #mod gives rem
        #div gives quotient
        r = num % 10        #removes last digit
        sum_of_powers += r ** 3 #armstrong num pow=3
        num = num // 10     # separates other digits from last digit
    
    return sum_of_powers == n

print(armstrong(371))  # True
print(armstrong(100))  # False
