###############################################
word = input("Enter a word: ")
vowels = "aeiouAEIOU"
result=""
for i in word:
    if i not in vowels:
        result += i
print(result)
################################################
even_count = 0
odd_count = 0
while True:
    num = int(input("Enter a number: (type 0 to stop)"))
    if num == 0:
        break
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    print("Even numbers:", even_count)
    print("Odd numbers:", odd_count)