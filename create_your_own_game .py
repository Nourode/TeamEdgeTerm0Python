#from zombie_manor_starter import Player


#setting: ("white_house"
#general: "save_the_president"

#input_msg = #an empty string
game_is_on = True
current_room = None

class Room:
    def __init__(self, name=None, description=None, objects=None, paths=None):
        self.name = name
        self.description = description
        self.objects = objects 
        self.paths = paths

class Player: 
  def __init__(self, name=None, items=[]):
      self.name =name
      self.items = items


player = Player("secret agent",["axe"]) 


weapons_room = Room()
weapons_room.name = "weapon room"
weapons_room. description = "the weapon_room has evreything you need to be able to break into the living_room  door it got guns and evereything you need to break the door"
weapons_room.objects = ["guns", "axe", "keys"]
weapons_room.paths =["living_room"]


living_room = Room()
living_room.name = "living_room"
living_room.description = "the living_room is a big room and it has a door that will lead you into the president room but it has a code that can make you open the president room there is random numbers around the walls that can help you figure out the code"
living_room.objects = ["tv", "codes", "chairs"]
living_room.paths = ["president room", "bathroom"]

bathroom = Room()
bathroom.name = "bathroom"
bathroom.description = "your in the bathroom you find more clues that can help you unlock the president room.  you also find the dead body of a secret service who has his walkie talkie in his hand"
bathroom.objects = ["towel","sink","mirrior"]
bathroom.paths = ["living_room"]

presidents_room = Room()
presidents_room.name="living_room"
presidents_room.description="You made it to the presidents_room which is empty, and a mess"
presidents_room.objects=("blood", "ear","secret_service agents body with missing leg")


# rooms list
Room.append("weapons_room")
Room.append("living_room")
Room.append("bathroom")
Room.append ("presidents_room")


def prompt_user():
    reply = ("what do you want do") 

    return reply

def check_answer(input):
  global current_room
  global input_msg
  global rooms

  print("checking input :  " +  input)
  input_msg = input


if "go" in input_msg:

    msg_array  = input_msg.split(" ")
    new_room = msg_array[1] ("ear found on floor")
    print(" player enters presidents room " + new_room)

    if new_room in "current_room".paths:
      print("Yes you can go there but be careful what you step on")

    
            index = rooms.index("room")
            current_room = rooms[index]
            print("You are now at the bathroom") : " + current_room.name")
      
      print ("You see a few thing: blood, a dead secret service agent, a broken walkie talkie")


    print("user " + object)


    elif "take" in input_msg:
        print("Taking ear...")

        items_list = input_msg.split(" ")
        item_to_take = items_list[1] 
     if item_to_take in current_room.objects:
          print("Yes you can take this item: " + item_to_take)
          player.items.append(item_to_take) 




#Guess the code to enter the presidents room

import random

#YOU ARE NOW OUTSIDE THE PRESIDENTS ROOM. Alarm goes off
# You need to stop it before zombies run towards the sound and attack you. FIGURE OUT CODE TO ENTER
class CodeGuessingGame:

    def __init__(self):
        ## define the range
        self.LOWER = 1
        self.HIGHER = 5

    def get_random_number(self):
        return random.randint(self.LOWER, self.HIGHER)

    
    def start(self):
        ## generating the passcode number
        random_number = self.get_random_number()

        print(
            f"Guess the randomly generated number from {self.LOWER} to {self.HIGHER}")

        ## heart of the game
        chances = 0
        while True:
            user_number = int(input("Enter the guessed number: "))
            if user_number == random_number:
                print(
                    f"-> Good job! You got it in {chances + 3} step{'s' if chances > 3 else ''}!")
                break
                print("Congratulations!! THE PRESIDENTS ROOM IS OPEN!!!")
            elif user_number < random_number:
                print("-> Your number is less than the passcode number")
            else:
                print("-> Your number is greater than the passcode number")
            chances += 1


if "guess_number_code" [open] == "passcode":
 "clear"()
 "print_passcode_accepted" ("passcode, guess_codes, guess_clue")
    

