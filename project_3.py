prices_usd = [10.50, 25.00, 150.00, 5.75, 200.00, 45.00]

prices_eur = [round(p * 0.92, 2) for p in prices_usd]

premium_items = [p for p in prices_usd if p > 100]

discounted = [p * 0.9 if p > 40 else p for p in prices_usd]

print(f"Original: {prices_usd}")
print(f"In EUR:   {prices_eur}")
print(f"Premium:  {premium_items}")
print(f"Discount: {discounted}")