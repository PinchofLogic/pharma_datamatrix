from expiry_date_validation import expiry_date_check #The Expiry validation module

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
            return f"INVALID BARCODE"

    if 'PPN' and 'BATCH' and 'EXPIRY' and 'SERIAL' in result.keys():
        if expiry_date_check(result['EXPIRY']) == False:
            return f'INVALID EXPIRY DATE'
        else:
            return result
    else:
        return f'INVALID BARCODE'


