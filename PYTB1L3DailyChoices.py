def vraag1():
    print ("\nYou're alarm rings... Do you get up or sleep?")
    print ("\n a: Get up \n b: Sleep")
    antwoord = input()
    if antwoord.lower() == "a":
        print ("\nYou're getting out of you're bed.")
        antwoord = input()
        vraag2()
    elif antwoord.lower() == "b":
        print ("\nYou're closing the alarm and keep sleeping.")
        antwoord = input()
        vraag2()
    else:
        print ("\nYou need to choose 'a' or 'b'")
        antwoord = input()
        vraag1()

def vraag2():
    print ("You need to do breakfast. What are you going to eat?")
    print ("\n a: Bread \n b: Nothing")
    antwoord = input()
    if antwoord.lower() == "a":
        print ("\nFirst you need to make one.")
        antwoord = input()
        vraag3()
    elif antwoord.lower() == "b":
        print ("\nNow you will be hungry and won't have enough energy.")
        antwoord = input()
        vraag3()
    else:
        print ("\nYou need to choose 'a' or 'b'")
        antwoord = input()
        vraag2()

def vraag3():
    print ("How do you want to go to school?")
    print ("\n a: With the bus \n b: With you're bike")
    antwoord = input()
    if antwoord.lower() == "a":
        print ("\nYou have 5 minutes left to be able to take the bus on time.")
        antwoord = input()
        vraag4()
    elif antwoord.lower() == "b":
        print ("\nYou first need to check if the tire is ok.")
        antwoord = input()
        vraag4()
    else:
        print ("\nYou need to choose 'a' or 'b'")
        antwoord = input()
        vraag3()

def vraag4():
    print ("You're back at home. Are you going to play videogames or make you're homework?")
    print ("\n a: Play videogames \n b: Make homework")
    antwoord = input()
    if antwoord.lower() == "a":
        print ("\nYou're starting the PlayStation.")
        antwoord = input()
        vraag5()
    elif antwoord.lower() == "b":
        print ("\nYou're taking you're laptop and making that boring homework.")
        antwoord = input()
        vraag5()
    else:
        print ("\nYou need to choose 'a' or 'b'")
        antwoord = input()
        vraag4()

def vraag5():
    print ("It's 00:00. Are you going to sleep or stay awaka?")
    print ("\n a: Going to sleep \n b: Staying awake")
    antwoord = input()
    if antwoord.lower() == "a":
        print ("\nDon't forget to brush you're teeth!!.")
        antwoord = input()
    elif antwoord.lower() == "b":
        print ("\nYou don't have sleep so just play some videogames.")
        antwoord = input()
    else:
        print ("\nYou need to choose 'a' or 'b'")
        antwoord = input()
        vraag5()


vraag1()