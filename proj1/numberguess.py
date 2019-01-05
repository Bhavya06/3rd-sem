import random

l = []
cpu = random.randint(1,100)
play = int(input("Enter a number between 1 to 100"))
l.append(play)

while play!=cpu:
    if play>cpu:
        print("HINT ! Try a smaller number ;)")
        play = int(input())
        l.append(play)
    else:
        print("HINT ! Try a bigger number ;)")
        play = int(input())
        l.append(play)
else:
    print("Congraaat! You got itt in ",len(l)," tries!")