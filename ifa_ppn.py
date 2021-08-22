"""
ASCII Code representation of a PPN code:
[)><30>06<29>9N 110375286414<29>1T12345ABCDE<29>D160617<29>S12345ABCDEF98765<30><4>

Actual Format including the ASCII chars is as below:

MACRO 06: The header [)> + ASCII 30 + ASCII 06 + ASCII 29 will be transmitted by the barcode reader before the data in the message and the trailer ASCII 30 + ASCII 4 will be transmitted afterwards.
OR
MACRO 05: The header [)> + ASCII 30 + ASCII 05 + ASCII 29 will be transmitted by the barcode reader before the data in the message and the trailer ASCII 30 + ASCII 4 will be transmitted afterwards. 

<29> is the GS separator. It’s used before the start of each identifier string. 

Identifier	Name	        Ex
9N	        PPN Code	    110375286414 (12 digits)
1T	        Batch	        12345-ABCDE (upto 20 digits)
D	        Expiry date	    160617 (YYMMDD)
S	        Serial number	12345ABCDEF98765 (between 12-20 chars)
8P	        GTIN	        08701234567896 (this is optional)

"""


from expiry_date_validation import expiry_date_check #The Expiry validation module
from ifa_ppn_validation import ppn_check

result = {'SCHEME': 'PPN'}

def ifa_ppn(barcode: str) -> dict: 

    while barcode:

        if barcode[:2] == '9N':
            result['PPN'] = barcode[2:14]
            if len(barcode) > 14:
                barcode = barcode[15:]
            else:
                barcode = None

        elif barcode[:1] == 'D':
            result['EXPIRY'] = barcode[1:7]
            if len(barcode) > 7:
                barcode = barcode[8:]
            else:
                barcode = None

        elif barcode[:2] == '1T':
            if chr(29) in barcode:
                for i, c in enumerate(barcode):
                    if ord(c) == 29:
                        result['BATCH'] = barcode[2:i]
                        barcode = barcode[i+1:]
                        break
            else:
                for i, c in enumerate(barcode):
                    if ord(c) == 30:
                        result['BATCH'] = barcode[2:i]
                        barcode = None
                
        elif barcode[:1] == 'S':
            if chr(29) in barcode:
                for i, c in enumerate(barcode):
                    if ord(c) == 29:
                        result['SERIAL'] = barcode[1:i]
                        barcode = barcode[i+1:]
                        break
            else:
                for i, c in enumerate(barcode):
                    if ord(c) == 30:
                        result['SERIAL'] = barcode[1:i]
                        barcode = None
        
        elif barcode[:2] == '8P':
            result['GTIN'] = barcode[2:16]
            if len(barcode) > 16:
                barcode = barcode[17:]
            else:
                barcode = None

        else:
            return {'ERROR': 'INVALID BARCODE'}

    if 'PPN' and 'BATCH' and 'EXPIRY' and 'SERIAL' in result.keys():
        if ppn_check(result['PPN']) == False and expiry_date_check(result['EXPIRY']) == False:
            return {'ERROR': 'INVALID PPN & EXPIRY DATE'}
        elif expiry_date_check(result['EXPIRY']) == False:
            return {'ERROR': 'INVALID EXPIRY DATE'}
        elif ppn_check(result['PPN']) == False:
            return {'ERROR': 'INVALID PPN'}
        else:
            return result
    else:
        return {'ERROR': 'INVALID BARCODE'}