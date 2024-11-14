import unittest
from mortgage.mortgage import Mortgage  # Adjust import according to your project structure
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class TestMortgage(unittest.TestCase):

    def test_invalid_loan_amount(self):
        print("Running test_invalid_loan_amount...")
        try:
            mortgage = Mortgage(-10000, "FIXED_5", "MONTHLY", 25)
        except ValueError as e:
            print("Caught ValueError as expected:", e)
        else:
            self.fail("ValueError was not raised")

    def test_invalid_rate(self):
        print("Running test_invalid_rate...")
        with self.assertRaises(ValueError):
            mortgage = Mortgage(100000, "INVALID_RATE", "MONTHLY", 25)

    def test_invalid_frequency(self):
        print("Running test_invalid_frequency...")
        with self.assertRaises(ValueError):
            mortgage = Mortgage(100000, "FIXED_5", "INVALID_FREQUENCY", 25)

    def test_invalid_amortization(self):
        print("Running test_invalid_amortization...")
        # Assuming 50 is outside the valid range for amortization years
        with self.assertRaises(ValueError):
            mortgage = Mortgage(100000, "FIXED_5", "MONTHLY", 50)

    def test_valid_inputs(self):
        print("Running test_valid_inputs...")
        mortgage = Mortgage(100000, "FIXED_5", "MONTHLY", 25)
        self.assertEqual(mortgage.loan_amount, 100000)
        self.assertEqual(mortgage.rate, MortgageRate.FIXED_5)
        self.assertEqual(mortgage.frequency, PaymentFrequency.MONTHLY)
        self.assertEqual(mortgage.amortization, 25)

    def test_valid_rate(self):
        print("Running test_valid_rate...")
        mortgage = Mortgage(100000, "FIXED_5", "MONTHLY", 25)
        self.assertEqual(mortgage.get_rate(), MortgageRate.FIXED_5)  # Checking if rate is correctly set

    def test_invalid_rate_assignment(self):
        print("Running test_invalid_rate_assignment...")
        try:
            mortgage = Mortgage(100000, "INVALID_RATE", "MONTHLY", 25)
        except ValueError as e:
            print("Caught ValueError as expected:", e)
        else:
            self.fail("ValueError was not raised for invalid rate")

if __name__ == "__main__":
    unittest.main()
