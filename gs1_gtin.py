"""
The function parse the GS1 Datamatrix barcode used for medicine packs.
The barcode scanners in the default setup outputs the scan is in below format:
]d201034531200000111719112510ABCD1234<GS>2110EW354EWER
(01)03453120000011(17)191125(10)ABCD1234<GS>(21)10EW354EWER
(01) = GTIN Identifier - Fixed 14 chars
(17) = Expiry Date Identifer - Fixed 6 Chars
(10) = Batch Identifier - Variable length. (upto 20 chars usually between 4 - 10 Chars)
(21) = Serial Number - Variable length. (upto 20 chars - Usually between 12 - 20 Chars)
(710 or 711 or 712 or 713 or 714) = Optional NHRN identifiers.
The symbology identifier ]d2 and for the second FNC1, when used as a separator character is <GS> Group-Separator.

"""


from .gs1_gtin_validation import gtin_check #The GTIN validation module
from .expiry_date_validation import expiry_date_check #The Expiry validation module

result = {'SCHEME': 'GS1'}


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
                if len(barcode) > 8:
                    barcode = barcode[8:]
                else:
                    barcode = None

            elif barcode[:2] == '10':
                if chr(29) in barcode:
                    index = barcode.index(chr(29))
                    result['BATCH'] = barcode[2:index]
                    barcode = barcode[index+1:]
                else:
                    result['BATCH'] = barcode[2:]
                    barcode = None
                    
            elif barcode[:2] == '21':
                if chr(29) in barcode:
                    index = barcode.index(chr(29))
                    result['SERIAL'] = barcode[2:index]
                    barcode = barcode[index+1:]
                else:
                    result['SERIAL'] = barcode[2:]
                    barcode = None


            elif barcode[:3] in ['710', '711', '712', '713', '714']:
                if chr(29) in barcode:
                    index = barcode.index(chr(29))
                    result['NHRN'] = barcode[3:index]
                    barcode = barcode[index+1:]
                else:
                    result['NHRN'] = barcode[3:]
                    barcode = None
            else:
                return {'ERROR': 'INVALID BARCODE', 'BARCODE': result}
    else:
        return {'ERROR': 'No GS Separator', 'BARCODE': result}

    if 'GTIN' and 'BATCH' and 'EXPIRY' and 'SERIAL' in result.keys():
        if gtin_check(result['GTIN']) == False and expiry_date_check(result['EXPIRY']) == False:
            return {'ERROR': 'INVALID GTIN & EXPIRY DATE', 'BARCODE': result}
        elif expiry_date_check(result['EXPIRY']) == False:
            return {'ERROR': 'INVALID EXPIRY DATE', 'BARCODE': result}
        elif gtin_check(result['GTIN']) == False:
            return {'ERROR': 'INVALID GTIN', 'BARCODE': result}
        else:
            return result
    else:
        return {'ERROR': 'INCOMPLETE DATA', 'BARCODE': result}
    

