## Nested loop with new condition ##

print("welcome to the rollcoaster")
height=int(input("what is your height in cm?"))
bill=0

if height>=120:
    age=int(input("what is your age? "))
    if age>=12 and age<=18:
        bill=7
        print("pay $7")
    elif age<12:
        bill=5
        print("pay $5")
    else:
        bill=12
        print("pay $12")
    
    wants_photo=input("do you want a photo taken? y 0r n")
    if wants_photo== "y":
        bill+=3
    print(f"your final bill{bill}")
else:
    print("sorry,you can't ride the rollcoaster")

