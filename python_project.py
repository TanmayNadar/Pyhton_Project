def rank_of_student(name, mark, updates, n):

    #list of the student
    x = [[0 for j in range(3)] for i in range(n)]
    for i in range(n):

        # here we store the name of the student
        x[i][0] = name[i]

        # here we update the marks of the student
        x[i][1] = mark[i] +updates[i]

        #here we store the current rank of the student
        x[i][2] =i+1

    maximum = x[0]
    for j in range(1,n):
        if (x[j][1] >= maximum[1]):
            maximum = x[j]

    #now printing the name and the jump of the student
    print("Name: ", maximum[0], ", jump:", abs(maximum[2]-1), sep="")


#input values:
n = int(input("Enter Total Numbers of Users: "))

name = []
for i in range(1,n+1):
    a = input("Enter your Name :")
    name.append(a)
print(name)

marks = []
for i in range(1,n+1):
    b = int(input("Enter your marks :"))
    marks.append(b)
print(marks)

updates = []
for i in range(1,n+1):
    c = int(input("Enter your update marks:"))
    updates.append(c)
print(updates)

#calling a function
n = len(marks)

rank_of_student(name,marks,updates,n)

