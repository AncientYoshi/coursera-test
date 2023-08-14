def calculate_tax(value, tax_rate):
    return round((value * tax_rate) / 100.00, 2)


print("Total tax", calculate_tax(149, 21))
