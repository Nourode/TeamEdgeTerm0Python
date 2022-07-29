#from zombie_manor_starter import Player


#setting: ("white_house"
#general: "save_the_president"

#input_msg = #an empty string
import random
game_is_on = True
current_room = None

global input_msg
global rooms

class Room:
    def __init__(self, name, description, objects, paths):
        self.name = name
        self.description = description
        self.objects = objects 
        self.paths = paths

class Player: 
  def __init__(self, name, items):
      self.name =name
      self.items = items


player = Player("secret agent",["axe", "gun"]) 

#user_input = ("")
outside=Room("outside","you are outside the white house",[],["weapons_room"])
weapons_room = Room("weapon room","the weapon_room has evreything you need to be able to break into the living_room door it got guns and evereything you need to break the door",["guns", "axe", "keys"],["living_room"]) 
living_room = Room("living_room", "the living_room is a big room and it has a door that will lead you into the president room but it has a code that can make you open the president room there is random numbers around the walls that can help you figure out the code",["tv", "codes", "chairs","tv"], ["codes", "chairs"])
bathroom = Room("bathroom","",["towel","sink","mirrior"],["living_room"])
presidents_room = Room("presidents_room","You made it to the presidents_room which is empty, and a mess",["blood", "ear","secret_service agents body with missing leg"],[living_room])


# rooms list

    


def prompt_user():
    reply = input("what do you want do?   ") 

    return reply

def check_answer(input):
  

    print("checking input :  " +  input)
    input_msg = input


    if input_msg == "enter white house weapons_room":

        msg_array  = input_msg.split(" ")
        new_room = msg_array[3]
        current_room= weapons_room
        print(" player enters " + new_room)

    #if new_room in current_room.paths:
        #print("Yes you can go there but be careful what you step on")
        #current_room = "rooms"[index]
       # print("You are now at the bathroom") :  "+ current_room.name"
        #print ("You see a few thing: bloody towel, bloody sink, bloody mirror")

        

       # print("user " + object)


    #elif "take" in input_msg:
        #print("Taking ear...")

           # items_list = input_msg.split(" ")
            #item_to_take = items_list[1] 
    #if item_to_take in current_room.objects:
          #print("Yes you can take this item: " + item_to_take)
          #player.items.append(item_to_take) 


    #if "go" in input_msg:

            #msg_array  = input_msg.split(" ")
            #new_room = msg_array[2] ("couch has bloody fingerprint")
            #print(" player enters living_room " + new_room)

   # if new_room in "current_room".paths:
           # print("Yes you may enter but watch the blood")
            #index = "rooms".index("room")
            #current_room = "rooms"[index]
            #print("You are now at the living_room" + " current_room.name")
            #print ("You see a few thing: tv news talking about zombies, fingerprint on couch, a keypad with a code")

        
           # print("user " + object)

    #if "take" in input_msg: 
        #print("Walking up to keypad...")

    #items_list = input_msg.split(" ")
    #item_to_take = items_list[1] 
    #if item_to_take in current_room.objects:
          #print("Yes you can use this item: " + item_to_take)
          #player.items.append(item_to_take) 




#Guess the code to enter the presidents room



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

        print({f"Guess the randomly generated number from {self.LOWER} to {self.HIGHER}"})

        ## heart of the game
        chances = 0
        while True:
            user_number = int(input("Enter the guessed number: "))
            if user_number == random_number:
                print(
                    f"-> Good job! You got it in {chances + 3} step{'s' if chances > 3 else ''}!")
                
                
                print("Congratulations!! THE PRESIDENTS ROOM IS OPEN!!!")
                break
            elif user_number < random_number:
                print("-> Your number is less than the passcode number")
            else:
                print("-> Your number is greater than the passcode number")
            chances += 1


        
                

        #if "go" in input_msg:

            #msg_array  = input_msg.split(" ")
           # new_room = msg_array[3] ("presidents room is a total mess")
            #print(" player enters presidents_room " + new_room)

        #if new_room in "current_room".paths:
           # print("Successfuly entered! Now watch out for the bodies")
            #index = "rooms".index("room")
            #current_room = "rooms"[index]
            #print("You are now at the presidents_room") 
            #print ("You see a few things: blood, ear, secret agent with missing leg")
        
            #print("user " + object)

        #elif "take" in input_msg:
            #print("taking secret agent to bury...")

        #items_list = input_msg.split(" ")
        #item_to_take = items_list[4] 
        #if item_to_take in current_room.objects:
          #print("Yes you can take this item RIP: " + item_to_take)
          #player.items.append(item_to_take) 

object Guessing Game:  


while game_is_on == True:
    print(outside.description)
    ans=prompt_user()
    check_answer(ans) 



