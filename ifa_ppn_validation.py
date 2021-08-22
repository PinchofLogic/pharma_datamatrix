"""
Each PPN requires two Modulo 97-calculated check digits for additional data integrity. 
To calculate the check digits, the ASCII value of the alphanumeric characters is used and multiplied 
by an ascending weight factor. The weighting of the digits starts on the left with two and increases 
by one for each following digit. The results of each multiplication are summed up and divided by 97, 
and the remainder are the check digits. If the remainder is only one digit, a leading zero is added.
"""

def ppn_check(ppn: str) -> bool:
    i = 0
    weight = 2
    digit_sum = 0
    for i in range(10):
        digit_sum += (ord(ppn[i]) * weight)
        weight += 1
    print(digit_sum)
    check_digit = digit_sum % 97
    return check_digit == int(ppn[-2:]) #PPN last two chars are converted to int to remove any leading zero.


