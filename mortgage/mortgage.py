from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION


"""
Description: A class meant to manage Mortgage options.
Author: 
Date: 
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""
class Mortgage:

 def __init__(self, loan_amount, rate, frequency, amortization):
     """
     This class is used to calculate the Loan
     Input needed:
     loan_amount = Principal Amount
     rate(float) = Annual intrest rate in percentages
     frequency(str) = Payment freq
     Amortization(int) = Number of Years
     """
     if loan_amount <= 0:
         raise ValueError("Loan Amount must be positive.")
     self.loan_amount = loan_amount
     try:
         self.__rate = MortgageRate[rate]
     except KeyError:
         raise ValueError("Rate provided is invalid.")
     try:
         self.__frequency = PaymentFrequency[frequency]
     except KeyError:
         raise ValueError("Frequency provided is invalid.")
     if amortization not in VALID_AMORTIZATION:
         raise ValueError("Amortization provided is invalid.")
     self.__amortization = amortization


