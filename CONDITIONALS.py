income = int(input("Enter your income: "))
if income < 85528:
    tax = (income * 0.18) - 556.02
    print(f"Tax: {round(tax)}")
else:
    tax = 14389.02 + (income - 85528) * 0.32
    print(f"Tax: {round(tax)}")