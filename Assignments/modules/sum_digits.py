def sum_digits(n):
    temp = n
    sum_is = 0
    while n!= 0:
        digit = n%10
        sum_is = sum_is+digit
        n = n//10
    return sum_is