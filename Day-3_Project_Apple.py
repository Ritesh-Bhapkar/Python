## Project Apple ##

print('''
        /)
   .-"".L,""-.
  ;       :.  :
  (       7:  )
   :         ;
    "..-"-.."
''')
print("welcome to the treasure island \nyour mission is to find the treasure")
ask=input("left or Right?")

if ask=="left":
    ask1=input("swim or wait")
    if ask1=="wait":
        ask2=input("which door?")
        if ask2=="yellow":
            print("You Win")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
