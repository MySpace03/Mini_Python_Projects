#library need for project
from random import randint

# we create list for objects i.e rock, paper and Scissors
# for an twist we give a super weapon to the computer only (just a little twist)
lts = ["Rock","Paper","Scissors","GUN"]

# for keeping scores we keep two counters one for player and one for computer
c_p = 0 # for player
c_c = 0 # for computer

# we create computer to play against human using list and radient function


# setting manual player to False
player = True

# lets start the game and run it until one wins the a game
while player==True:
    comp = lts[randint(0,3)]
    player = input("Rock, Paper or Scissors? ")
    if(player == comp):
        print("Its a tie")
    elif(player == "Rock"):
        if(comp == "GUN"):
            print("Pew pew boom boom bang The computer got ultimate Weapon to distroy you You lose!!😎")
            print("Game over!")
            c_c +=1;
        elif(comp == "Paper"):
            print("You lose! The computer choose: ",comp,"covers",player)
            c_c +=1
        elif (comp == "Scissors"):
            print("You win! the computer choose: ",comp,"will be smaches by",player)
            c_p +=1
    elif(player == "Paper"):
        if(comp == "GUN"):
            print("Pew pew boom boom bang The computer got ultimate Weapon to distroy you You lose!!😎")
            print("Game over!")
            c_c +=1
        elif(comp == "Rock"):
            print("You Win! The computer choose: ",comp,"will be covered by",player)
            c_p +=1
        elif (comp == "Scissors"):
            print("You lose! the computer choose: ",comp,"cuts",player)
            c_c += 1
    elif(player == "Scissors"):
        if(comp == "GUN"):
            print("Pew pew boom boom bang The computer got ultimate Weapon to distroy you You lose!!😎")
            print("Game over!")
            c_c +=1;
        elif(comp == "Rock"):
            print("You lose! The computer choose: ",comp,"will be smached by",player)
            c_c +=1
        elif (comp == "paper"):
            print("You win! the computer choose: ",comp,"will be cutted by",player)
            c_p += 1
    print("Score board: comp ",c_c,"\nYou",c_p)
    player = True
