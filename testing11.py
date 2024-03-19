# assign number to var 
result = 13
guess = int(input("Guess your number between (10,20) :"))

if guess > 13:
    print("Wrong Guess. Try Smaller")

elif guess < 13:
    print("Wrong Guess. Try Bigger")

elif guess == 13:
    print("Hoorary!")



