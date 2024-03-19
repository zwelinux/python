import random 


result = random.randint(1, 2)
choice = int(input(""" 
    Choose 
    Head for 1
    Tail for 2
"""))

if result == 1 and choice == 1:
    print("You Win. It's Head")

elif result == 2 and choice == 2:
    print("You Win. It's Tail")

elif result == 1 and choice == 2:
    print("You Loose. It's Head")

elif result == 2 and choice == 1:
    print("You Loose. It's Tail")

else:
    print("Something Went Wrong. Try Again")
