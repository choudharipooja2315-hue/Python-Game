# PROJECT 1: SNAKE, WATER, GUN GAME

''' here,
 1 = snake,
 -1 = water,
 0 = gun 
-----------------------------
Conditions :
Snake vs Water = Snake wins
Water vs Gun = Water wins
Gun vs Snake = Gun wins
Same choice = Draw
'''

import random
computer = random.choice([1,0,-1])

youstr = input("Enter you choice: ")
youDict = {"s":1, "w":-1 , "g":0}
reverseDict = {1:"snake", -1:"water", 0:"gun"}

you = youDict[youstr]

# Now here we have 2 variables - 'you' and 'computer'

print(f" You chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}")
# Now we sets conditions to check who wins!

if(computer == you):
    print("It's a draw")
else:
    if(computer == -1 and you ==1):
        print("You win!")

    elif(computer == -1 and you == 0):
        print("You lose, Computer won:(")

    elif(computer == 1 and you == -1):
        print("You lose, Computer won:(")

    elif(computer == 1 and you == 0):
        print("You win!")

    elif(computer == 0 and you == -1):
        print("You Won")

    elif(computer == 0 and you == 1):
        print("You lose, Computer won:( ")
    
    else:
        print("Something went wrong.")


