## Nested loop ##

print("welcome to the rollcoaster")
height=int(input("what is your height in cm?"))

if height>=120:
    age=int(input("what is your age? "))
    if age>=12 and age<=18:
        print("pay $7")
    elif age<12:
        print("pay $5")
    else:
        print("pay $12")
else:
    print("sorry,you can't ride the rollcoaster")
