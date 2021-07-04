import random

print("Game rules:\n 1. The players who scores 5 points first will win \n 2. For user input R = rock, P = Paper, S = Scissor ")
'''1 - Rock
   2 - Paper
   3 - Scissor'''

play = True
while(play == True):
    # initialise scores of user and computer as 0
    user = 0
    computer = 0 
    # for loop till one scores 5 points
    while(user != 5 and computer != 5):
        computer_input = random.randint(1,3) # generating random numbers between 1 and 3(both inclusive)
        # mapping numbers to R/P/S
        if computer_input == 1:
            computer_input = 'R'
        elif computer_input == 2:
            computer_input = 'P'
        else:
            computer_input = 'S'
        while(True):
            user_input = input("Enter R/P/S:   ").upper() # taking user input
            if user_input in ["R", "P", "S"]: # checking if user input is valid or not
                break
        # checking winner for each round
        if(user_input == "R"): 
            if(computer_input == "P"):
                computer += 1
            elif(computer_input == "S"):
                user += 1
        if(user_input == "P"):
            if(computer_input == "R"):
                user += 1
            elif(computer_input == "S"):
                computer += 1
        if(user_input == "S"):
            if(computer_input == "R"):
                computer += 1
            elif(computer_input == "P"):
                user += 1
        # print computer input
        print(f"Computer input: {computer_input}")
        # print user and computer's score
        print(f"USER   {user} : {computer}   COMPUTER\n\n")

    # Checking who has scored 5 points
    if(user == 5):
        print("Congratulations you win!!!!!!\n\n")
    else:
        print("Better Luck next time\n\n")

    # Asking if he wants to play again
    if((input("Want to Play Again[Y/y or N/n]:  ")) in ["n", "N"]):
        play = False
        print("Thanks for playing!!!")
