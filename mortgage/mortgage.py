from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

VALID_AMORTIZATION = {5, 10, 15, 20, 25, 30}


class Mortgage:
    def __init__(self, loan_amount, rate, frequency, amortization):
        if loan_amount <= 0:
            print("Loan amount validation failed.")
            raise ValueError("Loan Amount must be positive.")
        else:
            self.loan_amount = loan_amount

        # Use mutator to set rate
        self.rate = self.set_rate(rate)

        try:
            self.frequency = PaymentFrequency[frequency]
        except KeyError:
            raise ValueError("Frequency provided is invalid.")

        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        self.amortization = amortization

    # Mutator for rate: attempts to set the rate based on the given string
    def set_rate(self, rate):
        try:
            return MortgageRate[rate]  # Attempt to map the rate string to the enumeration
        except KeyError:
            raise ValueError("Rate provided is invalid.")  # Raise error if invalid

    # Accessor for rate: returns the value of the rate
    def get_rate(self):
        return self.rate
