list1 = []

while True:
    choice = int(input('''
    1. Push element
    2. Pop element
    3. Peek element
    4. Display element
    5. Exit

    Please enter a valid choice: '''
    ))

    if choice == 1:
        no = int(input(("Enter no. of elements to push: ")))
        for i in range(1, no+1):
            append = int(input(("Enter element to push: ")))
            list.append(append)
        print(list1)
    
    elif choice == 2:

        if len(list1) == 0:
            c1 = int(input(('''
            1. List is empty
            2. Do you want to add a new element
            Please enter a valid choice: ''')))
            if c1 == 1:
                print("Empty stack")
            elif c1 == 2:
                print("Enter element seperated by spaces: " , end="")
                l1 = list(map(int, input().split()))
                list1 = list1 + l1
                print(f"New list is {list1}")
                list1.pop()
                print(list1)
        else:
            list1.pop()
            print(list1)
        
        
    elif choice == 3:
        if len(list1) == 0:
            c1 = int(input(('''
            1. List is empty
            2. Do you want to add a new element
            Please enter a valid choice: ''')))
            if c1 == 1:
                print("Empty stack")
            elif c1 == 2:
                print("Enter element seperated by spaces: ", end = "")
                l1 = list(map(int, input().split()))
                list1 = list1 + l1
                print(f"New list is {list1}")
                print(list[-1])
            else:
                print("Not a valid choice")
        else:
            print(list1[-1])
    elif choice == 4:
        print("Display stack; ", list1)
    
    elif choice == 5:
        break
    
    else:
        print("please enter a valid choice.")

