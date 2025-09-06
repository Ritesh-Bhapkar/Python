student_heights=input("Input a list of student heights").split()
i=0
for n in range(0, len(student_heights)):
    student_heights[n]=int(student_heights[n])
    i=i+1

print(i)

sum=0
for j in student_heights:
    sum=sum+j
print(sum)

Average=round(sum/i)
print(Average)
