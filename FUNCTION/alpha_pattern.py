# Python implementation to print the
# pattern of alphabets A to Z using *

# Below height and width variable can be used
# to create a user-defined sized alphabet's pattern

# Number of lines for the alphabet's pattern

height = 5

# Number of character width in each line

width = (2 * height) - 1

# Function to find the absolute value
# of a number D


def abs(d):
    if d < 0:
        return -1*d
    else:
        return d

# Function to print the pattern of 'A'


def printA():

    n = width // 2
    for i in range(0, height):
        for j in range(0, width+1):
            if (j == n or j == (width - n) or (i == (height // 2) and j > n and j < (width - n))):
                print("*", end="")
            else:
                print(end=" ")
        print()
        n = n-1

# Function to print the pattern of 'B'


def printB():
    half = height // 2

    for i in range(0, height):
        print("*", end="")
        for j in range(0, width):
            if ((i == 0 or i == height - 1 or i == half) and j < (width - 2)):
                print("*", end="")
            elif (j == (width - 2) and not (i == 0 or i == height - 1 or i == half)):
                print("*", end="")
            else:
                print(end=" ")
        print()

# Function to print the pattern of 'C'


def printC():

    for i in range(0, height):
        print("*", end="")
        for j in range(0, height - 1):
            if (i == 0 or i == height - 1):
                print("*", end="")
            else:
                continue
        print()

# Function to print the pattern of 'D'


def printD():

    for i in range(0, height):
        print("*", end="")
        for j in range(0, height):
            if ((i == 0 or i == height - 1) and j < height - 1):
                print("*", end="")
            elif (j == height - 1 and i != 0 and i != height - 1):
                print("*", end="")
            else:
                print(end=" ")
        print()

# Function to print the pattern of 'E'


def printE():

    for i in range(0, height):
        print("*", end="")
        for j in range(0, height):
            if ((i == 0 or i == height - 1) or (i == height // 2 and j <= height // 2)):
                print("*", end="")
            else:
                continue
        print()

# Function to print the pattern of 'F'


def printF():

    for i in range(0, height):
        print("*", end="")
        for j in range(0, height):
            if ((i == 0) or (i == height // 2 and j <= height // 2)):
                print("*", end="")
            else:
                continue
        print()

# Function to print the pattern of 'G'


def printG():

    for i in range(0, height):
        for j in range(0, width-1):
            if ((i == 0 or i == height - 1) and (j == 0 or j == width - 2)):
                print(end=" ")
            elif (j == 0):
                print("*", end="")
            elif (i == 0 and j <= height):
                print("*", end="")
            elif (i == height // 2 and j > height // 2):
                print("*", end="")
            elif (i > height // 2 and j == width - 2):
                print("*", end="")
            elif (i == height - 1 and j < width - 1):
                print("*", end="")
            else:
                print(end=" ")
        print()

# Function to print the pattern of 'H'


def printH():

    for i in range(0, height):
        print("*", end="")
        for j in range(0, height):
            if ((j == height - 1) or (i == height // 2)):
                print("*", end="")
            else:
                print(end=" ")
        print()

# Function to print the pattern of 'I'


def printI():

    for i in range(0, height):
        for j in range(0, height):
            if (i == 0 or i == height - 1):
                print("*", end="")
            elif (j == height // 2):
                print("*", end="")
            else:
                print(end=" ")
        print()

# Function to print the pattern of 'J'


def printJ():

    for i in range(0, height):
        for j in range(0, height):
            if (i == height - 1 and (j > 0 and j < height - 1)):
                print("*", end="")
            elif ((j == height - 1 and i != height - 1) or (i > (height // 2) - 1 and j == 0 and i != height - 1)):
                print("*", end="")
            else:
                print(end=" ")
        print()

# Function to print the pattern of 'K'


def printK():
    half = height // 2
    dummy = half
    for i in range(0, height):
        print("*", end="")
        for j in range(0, half+1):
            if (j == abs(dummy)):
                print("*", end="")
            else:
                print(end=" ")
        print()
        dummy = dummy - 1

# Function to print the pattern of 'L'


def printL():

    for i in range(0, height):
        print("*", end="")
        for j in range(0, height+1):
            if (i == height - 1):
                print("*", end="")
            else:
                print(end=" ")
        print()

# Function to print the pattern of 'M'


def printM():
    counter = 0
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height+1):
            if (j == height):
                print("*", end="")
            elif (j == counter or j == height - counter - 1):
                print("*", end="")
            else:
                print(end=" ")
        if (counter == height // 2):
            counter = -99999
        else:
            counter = counter + 1

        print()

# Function to print the pattern of 'N'


def printN():
    counter = 0
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height+1):
            if (j == height):
                print("*", end="")
            elif (j == counter):
                print("*", end="")
            else:
                print(end=" ")
        counter = counter + 1
        print()

# Function to print the pattern of 'O'


def printO():
    space = height // 3
    width = height // 2 + height // 5 + space + space
    for i in range(0, height):
        for j in range(0, width + 1):
            if (j == width - abs(space) or j == abs(space)):
                print("*", end="")
            elif ((i == 0 or i == height - 1) and j > abs(space) and j < width - abs(space)):
                print("*", end="")
            else:
                print(end=" ")

        if (space != 0 and i < height // 2):
            space = space - 1
        elif (i >= (height // 2 + height // 5)):
            space = space - 1

        print()

# Function to print the pattern of 'P'


def printP():
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height):
            if ((i == 0 or i == height // 2) and j < height - 1):
                print("*", end="")
            elif (i < height // 2 and j == height - 1 and i != 0):
                print("*", end="")
            else:
                print(end=" ")
        print()

# Function to print the pattern of 'Q'


def printQ():
    printO()
    d = height
    for i in range(0, height//2):
        for j in range(0, d+1):
            if (j == d):
                print("*", end="")
            else:
                print(end=" ")
        print()
        d = d+1

# Function to print the pattern of 'R'


def printR():
    half = (height // 2)
    for i in range(0, height):
        print("*", end="")
        for j in range(0, width):
            if ((i == 0 or i == half) and j < (width - 2)):
                print("*", end="")
            elif (j == (width - 2) and not (i == 0 or i == half)):
                print("*", end="")
            else:
                print(end=" ")
        print()

# Function to print the pattern of 'S'


def printS():
    for i in range(0, height):
        for j in range(0, height):
            if ((i == 0 or i == height // 2 or i == height - 1)):
                print("*", end="")
            elif (i < height // 2 and j == 0):
                print("*", end="")
            elif (i > height // 2 and j == height - 1):
                print("*", end="")
            else:
                print(end=" ")
        print()

# Function to print the pattern of 'T'


def printT():
    for i in range(0, height):
        for j in range(0, height):
            if (i == 0):
                print("*", end="")
            elif (j == height // 2):
                print("*", end="")
            else:
                print(end=" ")
        print()

# Function to print the pattern of 'U'


def printU():
    for i in range(0, height):
        if (i != 0 and i != height - 1):
            print("*", end="")
        else:
            print(end=" ")
        for j in range(0, height):
            if (((i == height - 1) and j >= 0 and j < height - 1)):
                print("*", end="")
            elif (j == height - 1 and i != 0 and i != height - 1):
                print("*", end="")
            else:
                print(end=" ")
        print()

# Function to print the pattern of 'V'


def printV():
    counter = 0
    for i in range(0, height):
        for j in range(0, width+1):
            if (j == counter or j == width - counter - 1):
                print("*", end="")
            else:
                print(end=" ")

        counter = counter + 1
        print()

# Function to print the pattern of 'W'


def printW():
    counter = height // 2
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height+1):
            if (j == height):
                print("*", end="")
            elif ((i >= height // 2) and (j == counter or j == height - counter - 1)):
                print("*", end="")
            else:
                print(end=" ")
        if (i >= height // 2):
            counter = counter + 1
        print()

# Function to print the pattern of 'X'


def printX():
    counter = 0
    for i in range(0, height+1):
        for j in range(0, height+1):
            if (j == counter or j == height - counter):
                print("*", end="")
            else:
                print(end=" ")
        counter = counter + 1
        print()

# Function to print the pattern of 'Y'


def printY():
    counter = 0
    for i in range(0, height):
        for j in range(0, height+1):
            if (j == counter or j == height - counter and i <= height // 2):
                print("*", end="")
            else:
                print(end=" ")
        print()
        if (i < height // 2):
            counter = counter + 1

# Function to print the pattern of 'Z'


def printZ():
    counter = height - 1
    for i in range(0, height):
        for j in range(0, height):
            if (i == 0 or i == height - 1 or j == counter):
                print("*", end="")
            else:
                print(end=" ")
        counter = counter - 1
        print()


# Function print the pattern of the
# alphabets from A to Z

def printPattern(character):

    if character == 'A':
        return printA()
    elif character == 'B':
        return printB()
    elif character == 'C':
        return printC()
    elif character == 'D':
        return printD()
    elif character == 'E':
        return printE(),
    elif character == 'F':
        return printF(),
    elif character == 'G':
        return printG(),
    elif character == 'H':
        return printH(),
    elif character == 'I':
        return printI(),
    elif character == 'J':
        return printJ(),
    elif character == 'K':
        return printK(),
    elif character == 'L':
        return printL(),
    elif character == 'M':
        return printM(),
    elif character == 'N':
        return printN(),
    elif character == 'O':
        return printO(),
    elif character == 'P':
        return printP(),
    elif character == 'Q':
        return printQ(),
    elif character == 'R':
        return printR(),
    elif character == 'S':
        return printS(),
    elif character == 'T':
        return printT(),
    elif character == 'U':
        return printU(),
    elif character == 'V':
        return printV(),
    elif character == 'W':
        return printW(),
    elif character == 'X':
        return printX(),
    elif character == 'Y':
        return printY()
    else:
        printZ()


character = input("Enter the character in upper case : ").upper()
printPattern(character)
