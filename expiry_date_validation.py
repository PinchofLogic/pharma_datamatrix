"""
The expiry date is in the YYMMDD format in the EU FMD regulated barcodes. The program validates the expiry date. 
MM to be between valid values of 01 and 12. 
DD to be between valid values of 00 and 31. Taking account of months with date upto 30 days and Feb with 28 & 29 days. 
The logic also allows 00 for DD, this refers to the last day of the month. 

"""


from datetime import datetime


def expiry_date_check(e:str):
    my_year = e[:2]
    my_month = e[2:4]
    my_date = e[4:]
    
    if (int(my_month) not in range(1,13)):
        return False
    elif (int(my_date) not in range(32)):
        return False
    
    if my_date == '00':
        if my_month == '02' and int(my_year) % 4 == 0:
            my_date = '29'
        elif my_month == '02' and int(my_year) % 4 != 0:
            my_date = '28'
        elif my_month in ['01', '03', '05', '07', '08', '10', '12']:
            my_date = '31'
        else:
            my_date = '30'
    
    if my_month == '02' and int(my_year) % 4 == 0 and my_date <= '29':
        pass
    elif my_month == '02' and int(my_year) % 4 != 0 and my_date <= '28':
        pass
    elif my_month in ['01', '03', '05', '07', '08', '10', '12'] and my_date <= '31':
        pass
    elif my_month in ['04', '06', '09', '11'] and my_date <= '30':
        pass
    else:
        return False

    actual_date = my_year + my_month + my_date
    if actual_date > datetime.today().strftime('%y%m%d'):
        return True
    else:
        return False
    