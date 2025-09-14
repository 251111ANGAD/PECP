x = ['ab','cd']
index = 0

for i in x:
    x[index] = i.upper()
    index += 1

print(x) #This code works now

x = ['ab','cd']
for i in x:
    x.append(i.upper())
    print(x) #This code does not work as it creates an infinite loop