## LIST PROGRAM WITH RANDOM MODULE ##

names_string=input()
names=names_string.split(",")

import random
num_items=len(names)

random_choice=random.randint(0,num_items-1)
print(f"{names[random_choice]} is going to buy ticket")
