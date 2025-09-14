# HOMEWORK.PY
# PCEP - Python Certified Entry-Level Programmer
# Homework Assignment
age = int(input("Enter your age: "))
if age < 12 or age > 64:
    print("CRITICAL - HIGH PRIORITY")
elif age >= 12 and age <= 64:
    print("SERIOUS - MEDIUM PRIORITY")
else:
    print("STABLE - LOW PRIORITY")
# PCEP - Python Certified Entry-Level Programmer
# Homework Assignment
# create a program that calculates income tax based on income and deductions
income = float(input("Enter your income: "))
if income < 10000:
    tax = 0
elif income > 10000 and income <= 50000:
    tax = income * 0.1
else:
    tax = income * 0.2

health_insurance = input("Do you have health insurance? (yes/no): ").strip().lower()
if health_insurance == "yes":
    tax *= 0.95  # Apply 5% discount

donations = input("Did you make any donations? (yes/no): ").strip().lower()
if donations == "yes":
    tax *= 0.9  # Apply additional 10% discount

print(f"Your total tax is: ${tax:.2f}")