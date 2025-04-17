def leap_year(n):
    if (n%4==0 and n%100!=0) or (n%400==0):
        return f"{n} is a leap year."
    else:
        return f"{n} is not a leap year."