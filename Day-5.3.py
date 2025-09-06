## Maximium element from list ##

student_heights=input("Input a list of student heights").split()
i=0
for n in range(0, len(student_heights)):
    student_heights[n]=int(student_heights[n])
    i=i+1

max=student_heights[0]

for j in student_heights:
    if j>max:
        max=j
    else:
        max=max
print(max)
