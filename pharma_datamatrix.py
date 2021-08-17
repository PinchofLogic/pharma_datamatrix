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

from gs1_gtin import gs1_gtin
from ifa_ppn import ifa_ppn

def pharma_datamatrix(barcode: str, validation: bool = False) -> dict:
    """
    The function takes barcode string and return parsed objects in a `dict`. Optionally user can pass bool value to validate the barcode
    Parameters:
        barcode: string type. This is the barcode string with the <GS> seperators. 
        validation: bool type. If 'True' the function performs validation on GTIN and Expiry Date.
    Returns:
        dict: Returns dictionary object with GTIN, EXPIRY, BATCH, SERIAL & NHRN as keys.
    """
    if barcode[:3] == ']d2': #Most barcode scanners prepend ']d2' identifier for the GS1 datamatrix. This senction removes the identifier.
        barcode = barcode[3:]
        result = gs1_gtin(barcode)
    
    elif barcode[:2] in ['01', '21', '17', '10', '71']:
        result = gs1_gtin(barcode)

    elif barcode[:6] == '[)>'+chr(30)+'06':
        barcode = barcode[7:] # Removes the leading ASCII seperator after the scheme identifier.
        result = ifa_ppn(barcode)
   
    else:
        result = f"01 INVALID BARCODE"
        
    return result

