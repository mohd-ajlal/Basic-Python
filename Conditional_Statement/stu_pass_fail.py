name = input('Enter name of student: ')
sub = int(input('Enter no. of subject: '))
sum = 0
total = sub * 100
for i in range(1, sub + 1):
    marks = int(input(f'Enter marks of subject {i}: '))
    sum += marks
per = sum / total * 100
if per >= 35:
    print(f'{name} is pass and percentage is {per}')
else:
    print(f'{name} is fail and percentage is {per}')