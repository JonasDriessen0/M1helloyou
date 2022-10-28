from threading import Timer
import time

#alle quicktime functions staan hier
def quicktimetraining():
    timeout = 5
    t = Timer(timeout, print, ["You failed to press the button in time"])
    t.start()
    start_time = time.time()
    prompt = f"A quicktime event has started you have 5 seconds! (enter)\n"
    answer = input(prompt)
    t.cancel()
    end_time = time.time()
    reaction_time = end_time - start_time
    if reaction_time > timeout:
        print("You failed to press the button in time")
        dodge = False
    else:
        print("You completed this quicktime event")
        dodge = True

def quicktimedoor():
    timeout = 5
    t = Timer(timeout, print, ["You failed to grab onto something \n[Ending] You died"])
    t.start()
    start_time = time.time()
    prompt = f"Quickly grab onto something so you dont fall out of the car! (enter)\n"
    answer = input(prompt)
    t.cancel()
    end_time = time.time()
    reaction_time = end_time - start_time
    if reaction_time > timeout:
        print("You failed to grab onto something \n[Ending] You died")
        exit()
        dodge = False
    else:
        print("You grab onto the seat as to not fall out of the vehicle.")
        dodge = True

#hier staan alle functions voor de vragen
def q1():
    print("A. Stay")
    print("B. Leave")      
    awnser = input("")
    while True:
        if awnser == "A":
            print("You decide to go through with your plans")
            input("Press enter to continue:")
        elif awnser == "B":
            print("You change your mind last second and you leave never entering ukraine")
            print("[Ending] you left")
            exit()
        else:
            print(awnser + " isnt a valid awnser")
        break

def q2():
    print("A. Run as far away from any buildings as you can")
    print("B. Look for shelter")      
    awnser = input("")
    while True:
        if awnser == "A":
            print("You roughly guess where the missile is going and you run as far away from it as possible and you survive the attack watching how the missile strikes from afar")
            input("Press enter to continue:")
        elif awnser == "B":
            print("You run to the nearest building and many other people do aswell once inside you see a table and you decide "
            "to hide under it. The missiles comes down right next to your building and many parts of the buidling are crumbled "
            "you luckily survive but other people arent as lucky")
            input("Press enter to continue:")
            print("You see people struggling to get up from the rubble what do you do?")
            print("A. Help them")
            print("B. Try to get out of this building as fast as possible")      
            awnser = input("")
            while True:
                if awnser == "A":
                    print("You run over to help but just as your trying to help a soldier taps you on the back")
                    input("Press enter to continue:")
                elif awnser == "B":
                    print("You see an opening to the outside and your run for it but you trip on a piece of concrete and activate a chain reaction of the building collapsing")
                    print("[Ending] you died")
                    exit()
                else:
                    print(awnser + " isnt a valid awnser")
                break
        else:
            print(awnser + " isnt a valid awnser")
        break

def soldier():
    print("A. Go with him")
    print("B. Dont go with him")      
    awnser = input("")
    while True:
        if awnser == "A":
            print("He asks you to step into a car and you start driving somewhere you ask the soldier where youre going and he awnsers with 'Im bringing you to base youll get some training there'")
            input("Press enter to continue:")
        elif awnser == "B":
            print("You say that he probably has the wrong guy and that you wont go with him")
            input("Press enter to continue:")
            print("The soldier goes away,  what now?")
            print("A. Its still not too late to leave")
            print("B. Change your mind and go with the soldier")      
            awnser = input("")
            while True:
                if awnser == "A":
                    print("You decide its really not worth it and you leave")
                    input("[ending] you left")
                    exit()
                elif awnser == "B":
                    print("You realize your mistake and run after the soldier and apologize. He asks you to step into a car and you start driving somewhere you ask the soldier where youre going and he awnsers with 'Im bringing you to base youll get some training there'")
                    input("Press enter to continue:")
                else:
                    print(awnser + " isnt a valid awnser")
                break
        else:
            print(awnser + " isnt a valid awnser")
        break

def exp():
    print("A. Yes")
    print("B. A little bit") 
    print("C. None")     
    awnser = input("")
    while True:
        if awnser == "A":
            print("'Good, well come with me'")
            input("Press enter to continue:")
        elif awnser == "B":
            print("'Good, well come with me'")
            input("Press enter to continue:")
        elif awnser == "C":
            print("'Alright well ill teach you the basics'")
            input("Press enter to continue:")
        else:
            print(awnser + " isnt a valid awnser")
        break

def plan():
    print("A. Get supressing fire on the enemies so the other squads can move up")
    print("B. Wait it out") 
    print("C. get closer to the enemy")     
    awnser = input("")
    while True:
        if awnser == "A":
            print("You look at where the enemy fire is coming from, its a treeline on the other side of a field so you all start shooting at where you think the enemies are located.")
            input("Press enter to continue:")
        elif awnser == "B":
            print("'That wouldnt be a good idea soldier' A high ranking officer says we should supress the enemies so the other squads can move up")
            input("Press enter to continue:")
        elif awnser == "C":
            print("'That wouldnt be a good idea soldier' A high ranking officer says we should supress the enemies so the other squads can move up")
            input("Press enter to continue:")
        else:
            print(awnser + " isnt a valid awnser")
        break

def sitrep():
    print("A. Send other troops to head to the school")
    print("B. Go into the building and help") 
    print("C. Ignore it")     
    awnser = input("")
    while True:
        if awnser == "A":
            print("You feel as if you have done enough for today and you tell other troops of the situation, they emediatly head over")
            print("[Ending] The other troops sent in managed to clear the building of hostile activity, but you are questioned for not heading in yourself.")
            exit()
        elif awnser == "B":
            print("")
            input("Press enter to continue:")
        elif awnser == "C":
            print("You feel as if you have done enough for today and you decide to turn off the radio and ignore it")
            print("[Ending] Once you arrive at base you are questioned why you didnt go help the people at the school since it has now been taken over by enemies and the school attendants are being held hostage, you likely wont get very far if you keep doing this...")
            exit()
        else:
            print(awnser + " isnt a valid awnser")
        break

print("██╗░░░██╗██╗░░██╗██████╗░░█████╗░██╗███╗░░██╗███████╗  ███████╗░█████╗░██████╗░███████╗██╗░██████╗░███╗░░██╗" "\n"
"██║░░░██║██║░██╔╝██╔══██╗██╔══██╗██║████╗░██║██╔════╝  ██╔════╝██╔══██╗██╔══██╗██╔════╝██║██╔════╝░████╗░██║" "\n"
"██║░░░██║█████═╝░██████╔╝███████║██║██╔██╗██║█████╗░░  █████╗░░██║░░██║██████╔╝█████╗░░██║██║░░██╗░██╔██╗██║" "\n"
"██║░░░██║██╔═██╗░██╔══██╗██╔══██║██║██║╚████║██╔══╝░░  ██╔══╝░░██║░░██║██╔══██╗██╔══╝░░██║██║░░╚██╗██║╚████║" "\n"
"╚██████╔╝██║░╚██╗██║░░██║██║░░██║██║██║░╚███║███████╗  ██║░░░░░╚█████╔╝██║░░██║███████╗██║╚██████╔╝██║░╚███║" "\n"
"░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░╚═════╝░╚═╝░░╚══╝" "\n"
"██╗░░░░░███████╗░██████╗░██╗░█████╗░███╗░░██╗" "\n"
"██║░░░░░██╔════╝██╔════╝░██║██╔══██╗████╗░██║" "\n"
"██║░░░░░█████╗░░██║░░██╗░██║██║░░██║██╔██╗██║" "\n"
"██║░░░░░██╔══╝░░██║░░╚██╗██║██║░░██║██║╚████║" "\n"
"███████╗███████╗╚██████╔╝██║╚█████╔╝██║░╚███║" "\n"
"╚══════╝╚══════╝░╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝" "\n")
input("Pres enter to start:")
name = input("Hello, please enter your name:")
print("Welcome "+name+", This story is about a fighter joining the ukraine foreign legion and going on special missions to help gain intel for the ukrainian military. You will be playing as him throughout his entire journey and you will be making various choises that and into different outcomes so choose wisely.")
input("press enter to continue:")
print("[Arrival]")
print("As you step out of the train you can hear the announcer from the station say something in polish that you dont understand. "
"Youve arrived in the polish city of 'Rzeszów' from here on out you will be heading to the ukrainian border crossing."
"You step out of the station and a taxi was already waiting for you outside of the station, you step into the taxi and are "
"greeted by a man with a heavy slavic accent Welcome to poland my friend! I assume youre heading to border? he says in a friendly manner. "
"You nod and he starts driving, he doesnt says much for the rest of the drive and as you come closer to the border you see the traffic increase. "
"Many ukrainians are still trying to flee the country. You realize that this is your last chance to go back before youre too far gone")
print("do you want to leave?")
input("Press enter to continue:")
q1()
print("you arrive at the border and you're suprized at how easy it is to get into ukraine but not out of it. "
"Once you get through the border you can see military personel at a building and you start heading towards them "
"when all of a sudden you hear a faint rumbling noise, it almost sounds like a jet engine but then you see it. Its a missile and it appears to be headed"
" straight towards your location what do you do?")
input("Press enter to continue:")
q2()
print("A soldier recognizes you as one of the foreign legion sign ups and asks you to go with him")
soldier()
print("[training]")
print("You arrive at a military building where other people are housed and he takes you to the training building, "
"a high ranking soldier is waiting for you there. 'Hey soldier welcome to base, i assume youve had prior combat experience right?")
exp()
print("'Alright when your in the battlefield you need to act quick and make important decisions so thats what we are going to be practicing today' "
"This game has quicktime events, quicktime events are when you need to press a key within a limited amount of time to do a certain action. "
"As soon as you are ready we can start")
input("Press enter to start quicktime event:")
quicktimetraining()
print("'Well done soldier looks like your pretty much ready for the battlefield go to your weapon station and ill inform you on the mission'")
print("You go to grab your gear and weapons and head to the room where the info on the mission will be given.")
print("'Alright soldiers today your mission will be to assist other fighter who are in combat right now. "
"Entry will be done by vehicles but from then on it will be by foot. Does everyone understand? Good.")
input("press enter to continue:")
print("You and your other crew members rush to the vehicles, once inside your given orders to follow the others. "
"You sit in the backseat while another crew member is driving, bombs are falling all around you suddenly while in a sharp corner the car door on your side flies open")
input("press enter to continue:")
quicktimedoor()
print("'Jesus christ that was close'")
print("You soon arrive at the location and gunfire can be heard from multiple places, what is the plan?")
plan()
print("After that you get the orders to push up with the other squads and take enemy territory, so you and your crew push to the location and once you arrive you're informed that the position has been taken from the enemies"
" and you can return to base. You head to the car  but are informed of an alerting situation; a school with children still inside is"
" being captured by enemy forces")
print("What will you do?")
sitrep()
