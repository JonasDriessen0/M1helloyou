def q():
    print("A. ")
    print("B. ")      
    awnser = input("")
    while True:
        if awnser == "A":
            print("")
            input("Press enter to continue:")
        elif awnser == "B":
            print("")
            input("Press enter to continue:")
        else:
            print(awnser + " isnt a valid awnser")
        break

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

def q():
    print("A. ")
    print("B. ")      
    awnser = input("")
    while True:
        if awnser == "A":
            print("")
            input("Press enter to continue:")
        elif awnser == "B":
            print("")
            input("Press enter to continue:")
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
print("Welcome "+name+", This story is about a fighter joining the ukraine foreign legion and going on special missions to help gain intel for the ukrainian militar. You will be playing as him throughout his entire journey and you will be making various choises that and into different outcomes so choose wisely.")
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

