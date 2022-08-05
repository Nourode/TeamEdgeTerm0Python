class SecondFloor:
  # WHEN YOU CREATE A NEW OBJECT FOR THE SECOND FLOOR YOU CALL THIS METHOD TO RUN THE GAME.
  def playGameSecondFloor(self):

    choices = ["yes","no"]

    attacks = ["Pistol","Sniper","Uzi"]
    
    playerChoice = " "
     # while to validate/check in players text to make sure it's a valid options
    while playerChoice not in choices:
      
      playerChoice = input("you are on the second floor and you see a bloated zombie do you attack ? \n [yes , no ]")
      
      if playerChoice == 'yes':
        
        print("you have a uzi , a pistol and sniper which weapon you choose ? ")
        
        playerAttack = " "
        
        while playerAttack not in attacks:

          playerAttack = input(" Use the Uzi, Sniper, Pistol ")
          if playerAttack == "Uzi":
            print(" you shot down the bloater and the stomach exploded spreading toxic gas that kills you. ")
          elif playerAttack == "Pistol":
            print(" You fired at the belly and gas began to lead causing you to become sick and die. ")
          elif playerAttack == "Sniper":
            print(" You aimed for the head avoiding the gassy stomach and have cleared the floor. ")
            
      elif playerChoice == 'no':
        
        print("You begin to run and the floor below breaks and you die.")
    
# Class FirstFloor starts our game on the first floor

"""


"""

        
class FirstFloor:
  # method to start playing our game
  def playGameFirstFloor(self):
    # list to hold our choices for the player
    choices = ["yes","no"]
    # list to hold our attacks for the player
    attacks = ["Molotov cocktail","Rock","Machete"] ## make sure you use these attacks for the first floor.

    playerChoice = ""
    
    print ("Welcome to Evil Zombie for President.")

    # input prompt to hold the players name
    name = input("What is your name agent ? \n")
    print("Welcome Agent.Something is going on. People are not human anymore. Its a world that is filling up with the Walking Dead and the zombies invaded the White House. As a Secret Service Agent you were sent on a mission to get to the president before he turns into one. But watch out, you don't want to be bitten.")
    print("Welcome Agent: " + name + " we are on a very important mission to save the president from the zombie outbreak. Let's find the president")
    
    # Mission Start
    
    playerChoice = ""

    # while to validate/check in players text to make sure it's a valid options
    while playerChoice not in choices:
      
      playerChoice = input("You are in front of the white house do you enter or do you stay ? \n [yes , no ]")
      
      if playerChoice == 'yes':
        # print show the player thier options.
        print("You entered on the first floor and you see three zombies do you attack ? [yes , no].")
        playerchoice = input("")
        if playerChoice == 'yes':
            print ("You have a Molotov cocktail, Rock, and Machete which weapon do you choose ?.")

            playerAttack = " "

            while playerAttack not in attacks:

                playerAttack = input(" Use the Molotov cocktail , Rock, Machete")
                if playerAttack == "Molotov cocktail":
                    print (" You made a wall of fire and set the zombies on fire.")
                elif playerAttack == "Rock":
                    print (" You threw a rock across the hallway and the sound distracted the three zombies. ")
                elif playerAttack == "Machete":       
                    print ("You ran towards the zombies and chopped one of their heads off, you chopped the other zombies legs off, and you chopped the last zombies arms off")
                
                
        level2 = SecondFloor() 
        # created a new object to start the second floor of my game
        print(level2.playGameSecondFloor())
    
    

newGame = FirstFloor()

print(newGame.playGameFirstFloor())

