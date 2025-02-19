import os, time, random

#Este programa será un juego de dados

#--------------------------------------------------------------
#Functions
def rollingBase():
    print("Rolling.")
    time.sleep(0.5)
    os.system("cls" if os.name == "nt" else "clear")
    print("Rolling..")
    time.sleep(0.5)
    os.system("cls" if os.name == "nt" else "clear")
    print("Rolling...")
    time.sleep(0.5)
    os.system("cls" if os.name == "nt" else "clear")

def rolling():
    rollingBase()
    rollingBase()


#--------------------------------------------------------------


die = [1, 2, 3, 4, 5, 6]
keepPlaying = True


os.system("cls" if os.name == "nt" else "clear")
print("Welcome! This is a dice based game where you have to try to roll higher than the program does! You don't even have to do anything, just press enter and you can keep playing like a true gambler :D")
input("Press [Enter] to play > ")
os.system("cls" if os.name == "nt" else "clear")

while keepPlaying:
    

    computerDie1 = random.choice(die)
    computerDie2 = random.choice(die)

    computerRoll = computerDie1 + computerDie2

    #Computer roll ^^
    #--------------------------------------------------------------
    
    playerDie1 = random.choice(die)
    playerDie2 = random.choice(die)

    playerRoll = playerDie1 + playerDie2

    #Player roll ^^
    #--------------------------------------------------------------

    #--------------------------------------------------------------
    #Graphics
    rolling()
    print(f"""
          Computer roll = {computerRoll}
          ----------------------------
          Die 1 = {computerDie1}    |   Die 2 = {computerDie2}
          """)
    
    print(f"""
          Player roll = {playerRoll}
          ----------------------------
          Die 1 = {playerDie1}    |   Die 2 = {playerDie2}
          """)
    

    if computerRoll > playerRoll:
        print("""
               |   You Lost!  |
              """)
    elif computerRoll < playerRoll:
        print("""
               |   You Win!  |
              """)
    else:
        print("""
               |   Tie!  |
              """)

    #--------------------------------------------------------------

    #--------------------------------------------------------------
    #Run again 
    playAgain = input("Play again? >")
    if playAgain != "":
        break
print("Thanks for playing! Come back soon!")