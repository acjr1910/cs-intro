balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthly_interest_rate = annualInterestRate / 12.0


def calculate_year_debit(balance):
    for i in range(12):
        minimum_monthly_payment = monthlyPaymentRate * balance
        monthly_unpaid_balance = balance - minimum_monthly_payment
        balance = monthly_unpaid_balance + \
            (monthly_interest_rate * monthly_unpaid_balance)

    print('Remaining balance:', round(balance, 2))


calculate_year_debit(balance)
