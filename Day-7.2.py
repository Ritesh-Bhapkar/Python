import random
word_list=["ardvark","baboon","camel"]
chosen_word=random.choice(word_list)

print(f"pssst, the solution is {chosen_word}")

display=[""]

guess=input("guess a letter:").lower()


for letter in chosen_word:
    display=display+" "
    
print(display)
