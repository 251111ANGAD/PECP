list_a = [1]
list_b = list_a
list_b[0] = 0
print(list_a[0] == list_b[0])
print()
list_a = [1]
list_b = list_a[:]
list_b[0] = 0
print(list_a[0] == list_b[0])
