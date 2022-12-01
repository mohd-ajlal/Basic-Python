def vote(age):
    if age >= 18:
        print("You can vote")
    else:
        print("You can not vote")
# main
age = int(input("Enter age: "))
vote(age)