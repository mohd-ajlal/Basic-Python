import datetime

current_time1 = datetime.datetime.now()

name = input("Enter your name: ")

a= current_time1.hour
print(f"Current Hours is {a}")

if 0 <= a and a<4:
    print(f"Good Night {name}")
elif 4<= a and a <12:
    print(f"Good morning {name}")
elif 12<=a and a< 16:
    print(f"Good afternoon {name}")
elif 16 <= a and a< 21:
    print(f"Good eneving {name}")
elif 21<=a and a < 23:
    print(f"Good night {name}")
