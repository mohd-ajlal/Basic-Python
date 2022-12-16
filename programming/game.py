import random
num = random.randint(1, 100)
attempts = 10
while attempts:
    user_num = int(input("Guess the number b/w 1 to 100: "))
    attempts -= 1
    print("No. of attempts left: ", attempts)
    if user_num < num:
        print("Too small")
    elif user_num > num:
        print("Too large")
    else:
        print("You won!")
        break
else:
    print(f"You won to guess the number {num}")