#lesson #02: Loops & iteration
#lists - continued??

students = ['Sadia', 'Jordan', 'Alcina']

for student in students:
    print(student)


#we can also iterate over the numerical values or addresses
for i in range(len(students)):
    print(i+1)


#code for printing the list address plus the object in
#the given address


for i in range(len(students)):
    print(i+1, students[i])

