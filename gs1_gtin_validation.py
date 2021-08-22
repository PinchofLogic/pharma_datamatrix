"""
The function perform validation on the GS1-GTIN(14) based on the check digit detailed in the link below:
https://www.gs1.org/services/how-calculate-check-digit-manually

"""

def gtin_check(gtin: str):
    reverse_gtin = gtin[-2::-1] #Reversing the string without the check-digit
    digit_multipler3 = []
    digit_multipler1 = []

    for i, l in enumerate(reverse_gtin): 
        if i % 2 == 0:
            digit_multipler3.append(int(l))
        else:
            digit_multipler1.append(int(l))

    digit_sum = (sum(digit_multipler3) * 3) + sum(digit_multipler1)
    nearest_ten = round(digit_sum/10) * 10
    check_sum_digit = nearest_ten - digit_sum
    if check_sum_digit < 0:
        check_sum_digit = 10 + check_sum_digit
    return check_sum_digit == int(gtin[-1])

    
