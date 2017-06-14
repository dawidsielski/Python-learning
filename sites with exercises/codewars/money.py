def calculate_years(principal, interest, tax, desired):
    amount = principal
    year = 0
    while amount < desired:
        amount_after_interest = amount * interest + amount
        tax_amount = (amount_after_interest - amount) * tax
        amount_after_tax = amount_after_interest - tax_amount
        amount = amount_after_tax
        year += 1
    return year

print(calculate_years(1000, 0.05, 0.18, 1100))
