from random import randint

# we create list for objects i.e rock, paper and Scissors
# for an twist we give a super weapon to the computer only (just a little twist)
lts = ["Rock","Paper","Scissors","GUN"]

# for keeping scores we keep two counters one for player and one for computer
c_m = 0
c_c = 0

# we create computer to play against human using list and radient function
comp = lts[randint(0,3)]

# setting manual player to False
player = False

# lets start the game and run it until one wins the a game
while player==False:
    player = input("Rock, Paper or Scissors? ")
    if comp == player:
        print("Its a tie!")
    elif player=="Rock":
        if comp == "GUN":
            print("Pew pew boom boom bang The computer got ultimate Weapon to distroy you You lose!!😎")
            print("Game over!")
            c_c +=1
            player = True
        elif comp == "Paper":
            print("You win!","The computer choose:",comp,"Covers",player)
            c_m +=1
        else:
            print("You lose!","The computer choose:",comp,"Smaches",player)
            c_c +=1
    elif player == "Paper":
        if comp == "GUN":
            print("Pew pew boom boom bang The computer got ultimate Weapon to distroy you You lose!!😎")
            print("Game over!")
            c_c += 1
            player = True
        elif comp == "Scissors":
            print("You win!","The computer choose:",comp,"Covers",player)
            c_m +=1
        else:
            print("You lose!","The computer choose:",comp,"Smaches",player)
            c_c +=1
    elif player == "Scissors":
        if comp == "GUN":
            print("Pew pew boom boom bang The computer got ultimate Weapon to distroy you You lose!!😎")
            print("Game over!")
            c_c +=1
            player = True
        elif comp == "Paper":
            print("You win!","The computer choose:",comp,"Covers",player)
            c_m +=1
        else:
            print("You lose!","The computer choose:",comp,"Smaches",player)
            c_c +=1
    else:
        print("The entered Input is not correct check for speeling and caplital letters!")
    print("The Score of the game are:","\nComputer Score:",c_c,"\nYour Score:",c_m)
    player = False
    comp = lts[randint(0,3)]