import random

# 1 for Snake, -1 for Water, 0 for Gun
computer = random.choice([-1, 1, 0])

youstr = input("Enter your choice: ")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
'''
if computer == you:
    print("It's a draw!")
else:
    if (computer == 1 and you == -1): (computer-you)=2
        print("You lose!")       
    elif (computer == 1 and you == 0):(computer-you)=1
        print("You win!")        
    elif (computer == -1 and you == 1):(computer-you)=-2
        print("You win!")        
    elif (computer == -1 and you == 0):(computer-you)=-1
        print("You lose!")       
    elif (computer == 0 and you == -1):(computer-you)=1
        print("You win!")        
    elif (computer == 0 and you == 1):(computer-you)=-1
        print("You lose!")       
    else:
        print("Something went wrong!")

'''
if you == computer:
    print("It's a draw!")
elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
    print("You win!")
else:
    print("You lose!")
