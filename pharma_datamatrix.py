"""
This function contains code to identify the barcode type: GS1-GTIN or IFA-PPN.

"""

from gs1_gtin import gs1_gtin
from ifa_ppn import ifa_ppn

def pharma_datamatrix(barcode: str) -> dict:
    """
    The function takes barcode string and return parsed objects in a `dict`. 
    Optionally user can pass bool value to validate the barcode
    Parameters:
        barcode: string type. This is the barcode string with the <GS> seperators. 
     
    Returns:
        dict: Returns dictionary object with SCHEME, PPN, GTIN, EXPIRY, BATCH, SERIAL & NHRN as keys for valid requests 
        or relevant error strings.
    """
    if barcode[:3] == ']d2': #Most barcode scanners prepend ']d2' identifier for the GS1 datamatrix. This senction removes the identifier.
        barcode = barcode[3:]
        result = gs1_gtin(barcode)
    
    elif barcode[:2] in ['01', '21', '17', '10', '71']:
        result = gs1_gtin(barcode)

    elif barcode[:6] == ('[)>'+chr(30)+'06') or ('[)>'+chr(30)+'05'): # MACRO 06 or MACRO 05
        barcode = barcode[7:] # Removes the leading ASCII seperator after the scheme identifier.
        result = ifa_ppn(barcode)
   
    else:
        result = {'ERROR': 'INVALID BARCODE'}
        
    return result
