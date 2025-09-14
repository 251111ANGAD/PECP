# PCEP - Python Certified Entry-Level Programmer
# IF-ELSE.PY
NUM1=int(input("Enter first number: "))
NUM2=int(input("Enter second number: "))
if NUM1 > NUM2:
    print(NUM1 - NUM2)
elif NUM1 < NUM2:
    print(NUM1 + NUM2)
else:
    print(NUM1 * NUM2)
print()
# Leap Year Check
print("Leap Year Check\n________________________")
YEAR=int(input("Enter year: "))
if YEAR % 100 == 0 and YEAR % 400 == 0:
    print("IT IS A LEAP YEAR")
elif YEAR % 100 != 0 and YEAR % 4 == 0:
    print("IT IS A LEAP YEAR")
else:
    print("NOT A LEAP YEAR")
print()
