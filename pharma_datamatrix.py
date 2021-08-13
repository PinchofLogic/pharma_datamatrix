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

def pharma_datamatrix(barcode: str, validation: bool = False) -> dict:
    """
    The function takes barcode string and return parsed objects in a `dict`. Optionally user can pass bool value to validate the barcode
    Parameters:
        barcode: string type. This is the barcode string with the <GS> seperators. 
        validation: bool type. If 'True' the function performs validation on GTIN and Expiry Date.
    Returns:
        dict: Returns dictionary object with GTIN, EXPIRY, BATCH, SERIAL & NHRN as keys.
    """
    result = dict()
    result['NHRN'] = None
    if barcode[:3] == ']d2': #Most barcode scanners prepend ']d2' identifier for the GS1 datamatrix. This senction removes the identifier.
        barcode = barcode[3:] 
    while barcode:

        if barcode[:2] == '01':
            result['GTIN'] = barcode[2:16]
            barcode = barcode[16:]

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
                        result['NHRN'] = barcode[2:i]
                        barcode = barcode[i+1:]
                        break
            else:
                result['NHRN'] = barcode[2:]
                barcode = None

        else:
            return f"INVALID BARCODE"

# If the validtion is set to "True", below section is processed. Perform validation checks on GTIN and Expriry Date
    if validation:
        if gtin_check(result['GTIN']) == False and expiry_date_check(result['EXPIRY']) == False:
            return f'INVALID GTIN & EXPIRY DATE'
        elif expiry_date_check(result['EXPIRY']) == False:
            return f'INVALID EXPIRY DATE'
        elif gtin_check(result['GTIN']) == False:
            return f'INVALID GTIN'
        else:
            return result
    else:
        return result
