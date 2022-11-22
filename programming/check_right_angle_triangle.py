base = int(input('Enter base: '))
height = int(input('Enter height: '))
hypotenuse = int(input('Enter hypotenuse: '))
if base ** 2 + height ** 2 == hypotenuse ** 2:
    print('Right angle triangle')
else:
    print('Not a right angle triangle')