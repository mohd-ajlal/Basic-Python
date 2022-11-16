my_str = input('Enter a string: ').lower()

all_same = my_str == my_str[0] * len(my_str)

print(all_same)  # True or False

if all_same:

    print('All characters in the string are the same')
else:
    print('NOT all characters in the string are the same')