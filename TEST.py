import time

print("**With backslash r**")
for i in range(5):
    print(f"\rLoading {i}", end="")
    time.sleep(1)
print("\n")

print("**Without backslash r**")
for i in range(5):
    print(f"Loading {i}", end="")
    time.sleep(1)