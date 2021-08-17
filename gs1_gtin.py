from gs1_gtin_validation import gtin_check #The GTIN validation module
from expiry_date_validation import expiry_date_check #The Expiry validation module

result = {'SCHEME': 'GTIN'}


def gs1_gtin(barcode: str) -> dict: 
    
    if chr(29) in barcode:

        while barcode:

            if barcode[:2] == '01':
                result['GTIN'] = barcode[2:16]
                if len(barcode) > 16:
                    barcode = barcode[16:]
                else:
                    barcode = None

            elif barcode[:2] == '17':
                result['EXPIRY'] = barcode[2:8]
                barcode = barcode[8:]

            elif barcode[:2] == '10':
                if chr(29) in barcode:
                    for i, c in enumerate(barcode):
                        if ord(c) == 29:
                            result['BATCH'] = barcode[2:i]
                            barcode = barcode[i+1:]
                            break
                else:
                    result['BATCH'] = barcode[2:]
                    barcode = None
                    
            elif barcode[:2] == '21':
                if chr(29) in barcode:
                    #print("In the serial GS check")
                    for i, c in enumerate(barcode):
                        if ord(c) == 29:
                            result['SERIAL'] = barcode[2:i]
                            barcode = barcode[i+1:]
                            break
                else:
                    result['SERIAL'] = barcode[2:]
                    barcode = None


            elif barcode[:3] in ['710', '711', '712', '713', '714']:
                if chr(29) in barcode:
                    for i, c in enumerate(barcode):
                        if ord(c) == 29:
                            result['NHRN'] = barcode[3:i]
                            barcode = barcode[i+1:]
                            break
                else:
                    result['NHRN'] = barcode[3:]
                    barcode = None

            else:
                return f"INVALID BARCODE"
    
    else:
        return f"INVALID BARCODE"

    if 'GTIN' and 'BATCH' and 'EXPIRY' and 'SERIAL' in result.keys():
        if gtin_check(result['GTIN']) == False and expiry_date_check(result['EXPIRY']) == False:
            return f'INVALID GTIN & EXPIRY DATE'
        elif expiry_date_check(result['EXPIRY']) == False:
            return f'INVALID EXPIRY DATE'
        elif gtin_check(result['GTIN']) == False:
            return f'INVALID GTIN'
        else:
            return result
    

