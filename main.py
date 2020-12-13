import random

print("To stop PRess Q")
score=0
while True:
    num=random.randint(0,10)
    guess=input("Guess number etween 0 to 10:")
    if guess=='q':
        print('Game Over')
        break
    guess1=int(guess)
    if guess1 is num:
        print("YPU win")
        score +=10
        print('your new score is :',score)
    else:
        print("Your guess didn't match")
        print('The number was:',num)
