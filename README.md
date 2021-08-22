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
The first parameter 'barcode' is of 'string' type and its mandatory. The string should contain the <GS> seperator as per GS1 guidelines. 


Initial Import: 
from pharma_datamatrix import pharma_datamatrix

Example 1: Usage with validation (valid barcode)
    pharma_datamatrix('01085860077038511724123110HB5R21587E4QA11R')
Output: {'NHRN': None, 'GTIN': '08586007703851', 'EXPIRY': '241231', 'BATCH': 'HB5R1', 'SERIAL': '21587E4QA11R'}

Example 2: Usage without validation (Invalid barcode)
    pharma_datamatrix('085860077038511724113110HB5R21587E4QA11R')
Output: {'ERROR': 'INVALID BARCODE'}

Example 3: Usage with validation (valid barcode format but Invalid expiry date (31 Nov 24))
    pharma_datamatrix('01085860077038511724113110HB5R21587E4QA11R')
Output: {'ERROR': 'INVALID EXPIRY DATE'}

Example 4: Usage with validation (valid barcode format but Invalid GTIN)
    pharma_datamatrix('01083860077038511724113110HB5R21587E4QA11R')
Output: {'ERROR': 'INVALID GTIN'}

# Source
Github link: https://github.com/PinchofLogic/pharma_datamatrix

