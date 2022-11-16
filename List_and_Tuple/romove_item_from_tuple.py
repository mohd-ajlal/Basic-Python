tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("Original tuple: ", tup)

# Remove item from tuple

a = int(input("Enter a no. to remove from tuple: "))

# Method 1: Using list
tup = list(tup)
tup.remove(a)
tup = tuple(tup)
print("After removing 5 from tuple: ", tup)

# Method 2: Using slicing
tup = tup[:a-1] + tup[a:]
print("After removing 5 from tuple: ", tup)
