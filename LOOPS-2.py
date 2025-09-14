email = input("Enter your email: ")
output = ""
while True:
    for i in email:
        if i != "@":
            output += i
        else:
            break
    print("Output:", output)
    break