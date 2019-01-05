import random

while True:
    c = int(input("Enter choice 1:rock 2:paper 3:scissors"))
    while (c>3 or c<1):
        c = int(input("Enter valid input"))
    if(c==1):
        choice = "Rock"
    elif(c==2):
        choice = "Paper"
    else:
        choice = "Scissors"
    print("Your choice is ",choice)

    print("Now comp is playing")
    k = random.randint(1,3)
    if(k==1):
        cchoice = "Rock"
    elif(k==2):
        cchoice = "Paper"
    else:
        cchoice = "Scissors"
    print("Computer's choice is ",cchoice)

    result = ""

    if((c==1 and k==2) or (c==2 and k==1)):
        result = "Paper"
    elif((c==2 and k==3) or (c==3 and k==2)):
        result = "Scissors"
    elif((c==1 and k==3) and (c==3 and k==1)):
        result = "Rock"

    if(choice == result):
        print("Congrats! You win")
    if(cchoice == result):
        print("Computer wins!")
    elif(cchoice == choice):
        print("Draw!") 

    print("Do you want to continue? Y/N")
    m = input()

    if(m=='N' or m=='n'):
        break