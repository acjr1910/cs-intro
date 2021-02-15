balance = 3329
annualInterestRate = 0.2

monthly_interest_rate = annualInterestRate / 12.0
monthly_unpaid_balance = balance - minimum
balance = monthly_unpaid_balance + (monthly_interest_rate * balance)


def calculate_minimum_fixed(balance):
    return
