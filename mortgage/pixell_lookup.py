from enum import Enum
"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: {Student Name}
Date: {Date}
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, frequencies and amortization 
periods are used.
"""
class MortgageRate(Enum):
    """
    This Class defines about the Mortgage rate options with their rates of interest(both
    fixed and variable)
    FIXED_5: 0.0519
	FIXED_3: 0.0589
	FIXED_1: 0.0599
    VARIABLE_5: 0.0649
	VARIABLE_3: 0.0669
	VARIABLE_1: 0.0679
    """
    FIXED_5 = 0.0519
    FIXED_3 = 0.0589
    FIXED_1 = 0.0599
    VARIABLE_5 = 0.0649
    VARIABLE_3 = 0.0669
    VARIABLE_1 = 0.0679

class PaymentFrequency(Enum):
    """
    Different ways you can make mortgage payments. Just pick one.

    - MONTHLY: Pay 12 times a year. (that's once a month.)
    - BI_WEEKLY: Pay 26 times a year. (Every two weeks)
    - WEEKLY: Pay 52 times a year. (Once a week)
    """
    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52
VALID_AMORTIZATION = {5, 10, 15, 20, 25, 30}


help(MortgageRate)

