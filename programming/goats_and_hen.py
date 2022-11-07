# WAP in python to print no. of goats and hens in a poultry form by taking total no. of heads and total no. of legs from user.

# x = goat    y = hens

head = int(input("Enter total number of heads: "))
legs = int(input("Enter total number of legs: "))

x = (legs - 2 * head) /2

y = head - x

print(f"Goat is {x} and hens is {y}")