from PIL import Image
import time
def get_name():
    while True:
        name = input("Please enter your name:")
        if name.isalpha():
            break
        else:
            print("Invalid name.")
    print("Welcome: ",name, "Your purpose you must fufil is to slay the Great Fire Giant!")
def loss():
    print("You lose!")
    time.sleep(5)
    exit()       
#Final area of the adventure
def fire_giant():
    print("You proceed to go forward and climb up the mountain. You approach a chain bridge connecting a ravine together, and decide to cross it.")
    time.sleep(2)
    print("After crossing the chain bridge, you find the Fire Giant to be on the other side, in a big snowy field!")
    fire_giant = Image.open("fire giant.jpg")
    fire_giant.show()
    time.sleep(2)
    print("You walk up to him slowly.")
    rob = Image.open("rob.png")
    rob.show()
    prl = Image.open("prl.png")
    prl.show()
    w_choice = input("Will you fight him with Prelat's Infernal Crozier (P) or the Rivers of Blood Katana (K): ").upper()
    while True:
        if w_choice == "P":
            print("You strike the Fire Giant's big toe as hard as you can, and shatter is big toe. He screams in agony, and in a fluster of rage, he quickly scoops you up and tosses you with all his strength, off the mountain.")
            loss()
        elif w_choice == "K":
            print("You swiftly run underneath the fire giant, noticing his wounded left ankle. You begin to swing at it rapidly, and the Fire Giant quickly falls. You then stab him in his eye to finish him off.")
            time.sleep(3)
            print("With the Fire Giant slain, and your purpose fulfilled, you rest at a nearby bonfire and quickly fall asleep.")
            time.sleep(2)
            print("Great Job you have fulfilled your duty!")
            print("Exiting in 5 seconds.")
            time.sleep(5)
            exit()
        else:
            print("Invalid Input.")
            loss()
def malenia():
    print("You continue into the snowy and foggy fields, walking for quite a long time.")
    time.sleep(2)
    print("You approach a open field, where it is not foggy and Malenia is there!")
    malenia = Image.open("malenia.jpg")
    malenia.show()
    choice = input("Do you stand your ground and fight her (F) or do you run (R): ").upper()
    while True:
        if choice == "F":
            print("You walk towards her, ready to strike. She then jumps 10 feet into the air and dashes into you, cutting you into a million pieces with ease.")
            loss()
        elif choice == "R":
            print("You begin to run, getting pretty far this time. You turn around to see her thrusting her sword and dashing 50 feet forward, imapling you.")
            loss()
        else:
            print("Invalid Input")
            loss()
def mtops():
    m_tops = Image.open("mtops.jpg")
    m_tops.show()
    choice = input("You have entered the Mountain Tops of the Giants! Do you want to continue forward (F) or go left into the snowy field (L): ").upper()
    while True:
        if choice == "F":
            fire_giant()
        elif choice == "L":
            malenia()
        else:
            print("Invalid Input")
            loss()
#All the instances that can occur in the left of the ringed city
def rykard():
    print("You proceed to cross the bridge, noticing the massive pool of lava below. Once you reach the middle of the bridge, you notice the lava start bubbling. All of a sudden Rykard, Lord of Blasphemy emerges from the lava!")
    rykard = Image.open("rykard.jpg")
    rykard.show()
    time.sleep(1)
    print("You approach Rykard slowly.")
    time.sleep(1)
    spear = Image.open("spear.png")
    spear.show()
    blade = Image.open("blade.png")
    blade.show()
    w_choice = input ("Do you fight him with the serpent hunting spear (S) or with the blasphemous blade (B):").upper()
    while True:
        if w_choice == "S":
            print("You swing the great serpent hunting spear, and a beam of light forms, piercing rkyard with ease. The battle is long and hard, but eventually Rykard falls back to the depths beneath the bridge.")
            print("You continue your way down the bridge and reach the end, where there is a mysterious teleporter. You touch the teleport and you wake up in a mysterious place.")
            time.sleep(1)
            mtops()
        elif w_choice == "B":
            print("You run towards Rykard. Wielding the disgusting blade. You swing it at Rykard's body, but it deflects off his hard scales. Rykard then grabs you with his mouth and takes you to the depth beneath the bridge.")
            loss()
        else:
            print("Invalid input.")
            loss()
def ledo():
    print("You climb the tall ladder and upon reaching the top, you see Silver Knight Ledo and he begins to charge at you!")
    ledo = Image.open("ledo.jpg")
    ledo.show()
    time.sleep(1)
    print("He begins to get closer.")
    time.sleep(1)
    hammer=Image.open("hammer.png")
    hammer.show()
    greataxe=Image.open("greataxe.png")
    greataxe.show()
    w_choice2 = input("Do you fight him with a greataxe (G) or with Smough's Great Hammer (S): ").upper()
    while True:
        if w_choice2 == "G":
            print("You run towards Ledo doing a double front flip spinning slash attack and cut him clean in half.")
            print("You continue onward for quite a distance, walking through the Ringed city until you eventually find yourself in Boreal Valley.")
            time.sleep(4)
            mtops()
        elif w_choice2 == "S":
            print("You run towards Ledo, doing a jumping heavy hammer slam right on his head. It dents his helmet and Ledo swings his hammer back with 10x the force and takes your head off.")
            time.sleep(3)
            loss()
        else:
            print("Invalid Input")
            time.sleep(3)
            loss()
def l_rcity():
    path = input ("You proceed onward to the left of the ringed city. You approach a very tall ladder and long bridge. Do you climb the ladder (L) or cross the bridge (B): ").upper()
    while True:
        if path == "B":
            rykard()
        elif path == "L":
            ledo()
        else:
            print("Invalid Input.")
            loss()            
#All instances that can occur to the right of the ringed city
def beast():
    beast = Image.open("beast.jpg")
    beast.show()
    while True:
                beast = input("The beast clergyman appears! Do you fight him (F) or run away (R): ").upper()
                if beast == "F":
                    print("You swing your sword but realize the beast clergyman won't take any damage! He then proceeds to rip you in half with his bare hands and you die a very painful death.")
                    loss()
                elif beast == "R":
                    print("You turn around as fast as possible in an attempt to run away from him. You make it to the front door before he grabs your leg and rips you in half and you die a horrible death.")
                    loss()
                else:
                    print("Invalid input.")
                    loss()
def church():
    while True:
        choice = input("You enter the dark church. Do you continue forward (F) or take a right into that dark path (R): ").upper()
        if choice == "F":
            beast()
        elif choice == "R":
            print("You stumble your way through a dark hallway, following a faint light at the end. You make it to the light and stumble through a door and you find yourself in the Boreal Valley. ")
            mtops()
        else:
            print("Invalid input.")
            loss()
def greatsword():
    print("You run at the knight and swing your greatsword over your head and split the knight into two!")
    time.sleep(1)
def katana():
    print("You run towards the knight going for a spinning slash attack! You swing with all your might but your katanas deflect against his rock hard malformed black armor. The ringed knight then thrusts his flaming sword into and you die in agony.")
    time.sleep()
def dirt_path():
    while True:
        choice = input("You head down the dirt path and see a gang of ringed knights! Do you hide (H) or run (R): ").upper()
        if choice == "H":
            print("You hide in a nearby bush. You start crying of fear and the ringed knights notice the strange sounds and investigate. They find you curled up in the bush and take turns stabbing you to death")
            time.sleep(1)
            loss()
        elif choice == "R":
            print("You attempt to flee, but the quickly notice you. All of them start running after you and easily manage to catch up. They then kick you to the ground and pummel you to death.")
            time.sleep(1)
            loss()
        else:
            print("Invalid Input.") 
            loss()
def r_rcity():
    while True:
        image2 = Image.open("katana.png")
        image2.show()
        image3 = Image.open("greatsword.jpeg")
        image3.show()
        choice_r_rcity = input("You're approaching a ringed knight! Will you fight him with a great sword (G) or two katanas (K): ").upper()
        if choice_r_rcity == "G":
            greatsword()
            choice = input("After clearing the area of the ringed knight, you approach a church and a dirt path. Do you enter the church (E) or go down the dirt path (D): ").upper()       
            while True:
                if choice == "E":
                    church()
                elif choice == "D":
                    dirt_path()
                else:
                    print("Invalid input.")
        elif choice_r_rcity == "K":
            katana()
            loss()
        else:
            print("Invalid input.")
            loss()

def adventure():
    get_name()
    image1 = Image.open("rcity.jpg")
    image1.show()
    while True:
        choice = input("You are approaching the Ringed City and there are two seperate paths. Do you go left (L) or right (R): ").upper()
        if choice == "R":
            r_rcity()
        elif choice == "L":
            l_rcity()
        else:
            print("Invalid input.")
            loss()

while True:
    startup = input("Do you want to go on an adventure (Y) or (N): ").upper()
    if startup == "Y":
        adventure()
    elif startup == "N":
        print("Okay, maybe next time!")
        time.sleep(5)
        exit()
    else:
        print("Invalid input.")