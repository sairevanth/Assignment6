import unittest
from mortgage.mortgage import Mortgage  # Adjust import according to your project structure
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class TestMortgage(unittest.TestCase):

    def test_invalid_loan_amount(self):
        print("Running test_invalid_loan_amount...")
        with self.assertRaises(ValueError):
            Mortgage(-1000, "FIXED_5", "MONTHLY", 25)

    def test_invalid_rate(self):
        print("Running test_invalid_rate...")
        with self.assertRaises(ValueError):
            Mortgage(100000, "INVALID_RATE", "MONTHLY", 25)

    def test_invalid_frequency(self):
        print("Running test_invalid_frequency...")
        with self.assertRaises(ValueError):
            Mortgage(100000, "FIXED_5", "INVALID_FREQUENCY", 25)

    def test_invalid_amortization(self):
        print("Running test_invalid_amortization...")
        # Assuming 30 is outside the valid range
        with self.assertRaises(ValueError):
            Mortgage(100000, "FIXED_5", "MONTHLY", 50)
    def test_valid_inputs(self):
        print("Running test_valid_inputs...")
        mortgage = Mortgage(100000, "FIXED_5", "MONTHLY", 25)
        self.assertEqual(mortgage.loan_amount, 100000)
        self.assertEqual(mortgage.rate, MortgageRate.FIXED_5)
        self.assertEqual(mortgage.frequency, PaymentFrequency.MONTHLY)
        self.assertEqual(mortgage.amortization, 25)

if __name__ == "__main__":
    unittest.main()
