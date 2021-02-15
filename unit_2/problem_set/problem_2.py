balance = 3926
annualInterestRate = 0.2

monthly_interest_rate = annualInterestRate / 12.0


def calculate_minimum_fixed(balance):
    unpaid_balance = balance
    fixed_monthly_payment = 0
    while unpaid_balance > 0:
        for month in range(12):
            unpaid_balance = unpaid_balance - fixed_monthly_payment
            unpaid_balance = unpaid_balance + \
                (monthly_interest_rate * unpaid_balance)
        if unpaid_balance > 0:
            fixed_monthly_payment += 10
            unpaid_balance = balance
        else:
            break
    return print('Lowest Payment:',  fixed_monthly_payment)


calculate_minimum_fixed(balance)
