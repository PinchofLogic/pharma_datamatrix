# pharma_datamatrix package
The package allow users to pass the string produced by the 2D barcode scanners and parse the string into GTIN, EXPIRY, SERIAL, BATCH and NHRN.
Optionally, user can pass validation=True, to validate the GTIN and Expiry date.

# Files
pharma_datamatrix.py: Primary file with the parsing logic. Is the string is valid, it will return a dict of the values. Otherwise return invalid string.

expiry_date_validation.py: This files contains the logic that validates the Expiry date. This file checks if the YYMMDD contains valid digits. Ex: MM to be between 01 & 12. And if the expiry date greater than the date of the scan: i.e. not is valid past date.

gs1_gtin_validation.py: This file contains the logic that validates the GS1 - GTIN(14).

# Installation 
To install the package please run the below command:
pip install pharma_datamatrix

# Usage
The function pharma_datamatrix(barcode: str, Validation: bool = False) takes two parameters:
The first parameter 'barcode' is of 'string' type and its mandatory. The string should contain the <GS> seperator as per GS1 guidelines. 
The second parameter 'validation' is of bool type and default to 'False'. Users can pass 'True' for the package to perform validation on GTIN and Expiry Date. 

Initial Import: 
from pharma_datamatrix import pharma_datamatrix

Example 1: Usage without validation (Expiry date is invalid but no validation is performed)
    pharma_datamatrix('01085860077038511724113110HB5R121587E4QA11R')
Output: {'NHRN': None, 'GTIN': '08586007703851', 'EXPIRY': '241131', 'BATCH': 'HB5R1', 'SERIAL': '21587E4QA11R'}

Example 2: Usage without validation (Invalid barcode)
    pharma_datamatrix('085860077038511724113110HB5R21587E4QA11R')
Output: INVALID BARCODE

Example 3: Usage with validation (valid barcode)
    pharma_datamatrix('01085860077038511724123110HB5R21587E4QA11R', True)
Output: {'NHRN': None, 'GTIN': '08586007703851', 'EXPIRY': '241231', 'BATCH': 'HB5R1', 'SERIAL': '21587E4QA11R'}

Example 4: Usage with validation (valid barcode format but Invalid expiry date (31 Nov 24))
    pharma_datamatrix('01085860077038511724113110HB5R21587E4QA11R', True)
Output: INVALID EXPIRY DATE

Example 5: Usage with validation (valid barcode format but Invalid GTIN)
    pharma_datamatrix('01083860077038511724113110HB5R21587E4QA11R', True)
Output: INVALID GTIN

# Source
Github link: https://github.com/PinchofLogic/pharma_datamatrix

