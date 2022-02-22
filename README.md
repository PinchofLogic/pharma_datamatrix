# pharma_datamatrix package
The package allow users to pass the string produced by the 2D barcode scanners and parse the string into GTIN, PPN, EXPIRY, SERIAL, BATCH and NHRN.

# Files
pharma_datamatrix.py: Primary function that checks the barcode format and inturn calls relevant parsing logic function.

gs1_gtin.py: Parse the GS1 GTIN barcode string and validate GTIN & Expiry.

ifa_ppn.py: Parse the IFA PPN barcode string (MACRO 06 & MACRO 05) and validate PPN & Expiry.

expiry_date_validation.py: This files contains the logic that validates the Expiry date. This file checks if the YYMMDD contains valid digits. Ex: MM to be between 01 & 12. And if the expiry date greater than the date of the scan: i.e. not is valid past date.

gs1_gtin_validation.py: This file contains the logic that validates the GS1 - GTIN.

ifa_ppn_validation.py: This file contains the logic to validate IFA PPN format.


# Installation 
To install the package please run the below command:
pip install pharma_datamatrix

# Usage
The function pharma_datamatrix(barcode: str):
The 'barcode' parameter is of 'string' type and its mandatory. The string should contain the <GS> seperator as per GS1 guidelines. 


Initial Import: 
from pharma_datamatrix import pharma_datamatrix

Example 1: Valid GS1 barcode
    pharma_datamatrix(']d201085860077038511724123110HB5R21587E4QA11R')
Output: {'SCHEME': 'GS1', 'GTIN': '08586007703851', 'EXPIRY': '241231', 'BATCH': 'HB5R1', 'SERIAL': '21587E4QA11R'}

Example 2: Valid PPN barcode
    pharma_datamatrix('9N#03752864#1T#12345ABCDE#D#260617#S#12345ABCDEF98765')
Output: {'SCHEME': 'IFA', 'PPN': '03752864', 'EXPIRY': '260617', 'BATCH': '12345ABCDE', 'SERIAL': '12345ABCDEF98765'}

Example 3: Invalid barcode (Invalid format)
    pharma_datamatrix('085860077038511724113110HB5R21587E4QA11R')
Output: {'ERROR': 'INVALID FORMAT','BARCODE': '085860077038511724113110HB5R21587E4QA11R'}

Example 4: Invalid barcode (valid barcode format but Invalid expiry date (31 Nov 24))
    pharma_datamatrix('01085860077038511724113110HB5R21587E4QA11R')
Output: {'ERROR': 'INVALID EXPIRY DATE', 'BARCODE': {'SCHEME': 'GS1', 'GTIN': '08586007703851', 'EXPIRY': '241131', 'BATCH': 'HB5R1', 'SERIAL': '21587E4QA11R'}}

Example 5: Invalid barcode (valid barcode format but Invalid GTIN)
    pharma_datamatrix('01243556547871161724011310TEST3C7E76935A')
Output: {'ERROR': 'INVALID GTIN', 'BARCODE': {'SCHEME': 'GS1', 'GTIN': '24355654787116', 'EXPIRY': '240113', 'BATCH': 'TEST3C7E76935A', 'SERIAL': 'PK133CBABE6C85F2C4A'}}

# Source
Github link: https://github.com/PinchofLogic/pharma_datamatrix

