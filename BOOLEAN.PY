number = int(input("Enter a number: "))
condition = "\nEVEN" if number % 2 == 0 else "\nODD"
print(condition)
condition = "\nNEGATIVE" if number < 0 else "\nPOSITIVE"
print(condition)

distance = int(input("Enter a distance (in miles): "))
age = int(input("Enter your age: "))
if distance < 1000:
    if age < 12:
        print("$200")
    elif age > 11 and age < 65:
        print("$300")
    elif age > 64:
        print("$250")
    else:
        print("INVALID INPUT")
else:
    if age < 12:
        print("$400")
    elif age > 11 and age < 65:
        print("$500")
    elif age > 64:
        print("$450")
    else:
        print("INVALID INPUT")
    