balance = 320000
annualInterestRate = 0.2


def calc_minimum_pay(balance, interest):
    monthly_interest_rate = interest / 12.0
    lower_bound = balance / 12
    upper_bound = (balance * (1 + monthly_interest_rate) ** 12) / 12
    unpaid_balance = balance
    fixed_payment = 0

    while unpaid_balance > 0:
        payment_guess = (lower_bound + upper_bound) / 2

        for month in range(12):
            unpaid_balance = unpaid_balance - payment_guess
            unpaid_balance = unpaid_balance + \
                (monthly_interest_rate * unpaid_balance)

        if round(lower_bound, 3) == round(upper_bound, 3):
            fixed_payment = payment_guess
            break
        elif unpaid_balance > 0:
            lower_bound = payment_guess
            unpaid_balance = balance
        elif unpaid_balance < 0:
            upper_bound = payment_guess
            unpaid_balance = balance

    return print('Lowest Payment:', round(fixed_payment, 2))


calc_minimum_pay(balance, annualInterestRate)
