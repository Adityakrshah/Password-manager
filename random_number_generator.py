import random
A,B=map(int,input("enter range of numbers:").split())
print(f"Your Range of numbers are {A} to {B}\n")
print("Let's Start the game:\n")
win=0

while True:
    win+=1
    user=int(input("Guess any number between your given range:"))
    guess=random.randint(A,B)
    if user==guess:
        print(f"YAY!!you guessed it correct in {win} times!!")
        break
    else:
        print(f"Sorry!! Please try again!")
        continue
