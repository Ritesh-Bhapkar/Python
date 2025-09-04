## Pizza order Automation ##
print("Welcome to Python Pizza Deliveries")
size=input("what size pizza do you want? S,M,L : ")
add_papperoni=input("do you want pepperoni? y or n : ")
extra_cheese=input("extra cheese for any pizza : ")

Pepperoni=0

if size=="S":
    bill=15
    print("small pizza price is $15" )
elif size=="M":
    bill=20
    print("medium pizza price is $20")
else:
    bill=25
    print("Large pizza price is $25")

if add_papperoni=="y":
    if size=="S":
        bill=bill+2
    else:
        bill=bill+3

if extra_cheese=="y":
    bill+=1
print(f"your total bill is: {bill}")
