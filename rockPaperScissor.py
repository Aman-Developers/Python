# Here we are practicing the same topic random to make this game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


myList = [rock, paper, scissor]



print("Welcome to Rock, Paper, Scissors Game")
print("Enter 1 for Rock, 2 for Paper, 3 for Scissor")

choice = int(input("Enter your Choice : "))
computer = random.randint(0,2)

# print(myList[computer])

if choice == 1:
    print(rock)
    if computer == 0:   # rock
        print("Computer Choice : ")
        print(myList[0])
        print("Game Draw")

    elif computer == 1:  # paper
        print("Computer Choice : ")
        print(myList[1])
        print("You Lose")

    elif computer == 2:  # scissor
        print("Computer Choice : ")
        print(myList[2])
        print("You win!")
    
    
    
elif choice == 2:
    print(paper)
    
    if computer == 0:
        print("Computer Choice : ")
        print(myList[0])
        print("You Win!")

    elif computer == 1:
        print("Computer Choice : ")
        print(myList[1])
        print("Game Draw")

    elif computer == 2:
        print("Computer Choice : ")
        print(myList[2])
        print("You Lose")


elif choice == 3:
    print(scissor)

    if computer == 0:
        print("Computer Choice : ")
        print(myList[0])
        print("You Lose")

    elif computer == 1:
        print("Computer Choice : ")
        print(myList[1])
        print("You Win!")

    elif computer == 2:
        print("Computer Choice : ")
        print(myList[2])
        print("Game Draw")
else:
    print("Invalid Choice")


