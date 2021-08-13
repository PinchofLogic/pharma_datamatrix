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

    actual_date = my_year + my_month + my_date
    if actual_date > datetime.today().strftime('%y%m%d'):
        return True
    else:
        return False
    