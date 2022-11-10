list = []
stu = int(input("Enter no. of students: "))
for i in range(1, stu+1):
    marks = int(input(f"Enter marks of {i} student: "))
    list.append(marks)
list.sort()
print(list)

