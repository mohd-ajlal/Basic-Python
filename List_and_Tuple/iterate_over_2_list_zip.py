# zip is used to iterate over 2 list at a time
# if there is a mismatch in the length of the list, it will stop at the shortest list

# Example 1 
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3, 4, 5]
output = zip(list1, list2)
print(list(output))  # 👉️ [('a', 1), ('b', 2), ('c', 3)]

# Example 2 - using for loop

l1 = [10, 20, 30, 40]
l2 = [100, 200, 300, 400]

for a, b in zip(l1, l2):
    print(a, b)