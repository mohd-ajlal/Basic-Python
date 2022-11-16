my_tuple = ('a', 'b', 'c')

a = input('Enter a character: ')

my_list = list(my_tuple)
my_list.insert(3, a)

new_tuple = tuple(my_list)
print(new_tuple)  # 👉️ ('a', 'b', 'c', 'd')