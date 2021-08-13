"""
The function perform validation on the GS1-GTIN(14)

"""

def gtin_check(g: str):
    digit_sum = (int(g[0]) * 3) + int(g[1]) + (int(g[2]) * 3) + int(g[3]) + (int(g[4]) * 3) + int(g[5]) + (int(g[6]) * 3) + int(g[7]) + (int(g[8]) * 3) + int(g[9]) + (int(g[10]) * 3) + int(g[11]) + (int(g[12]) * 3)
    nearest_ten = round(digit_sum/10) * 10
    check_sum_digit = nearest_ten - digit_sum
    return check_sum_digit == int(g[-1])

