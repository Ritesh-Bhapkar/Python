import random
word_list=["ardvark","baboon","camel"]
chosen_word=random.choice(word_list)
guess=input("guess the letter").lower()

for letter in chosen_word:
    if guess==letter:
        print("right")
    else:
        print("false")
