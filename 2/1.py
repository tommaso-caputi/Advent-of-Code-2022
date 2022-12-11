#  rock  =    A, X -> 1              
#  paper =    B, Y -> 2
#  scissors = C, Z -> 3
#  1>3, 3>2 2>1
with open("2.txt","r") as f:
    list = f.readlines()

rounds = []
for line in list:
    round = []
    v = "1" if line[0]=="A"  else "2" if line[0]=="B"  else "3"
    round.append(v)
    v = "1" if line[2]=="X"  else "2" if line[2]=="Y"  else "3"
    round.append(v)
    rounds.append(round)

sum = 0
for round in rounds:
    win = "no"
    sum+=int(round[1])
    print(sum)
    if round[1]==round[0]:
        win = "draw"
    else:
        if round[1] == "1" and round[0] == "3":
            win = "yes"
        elif round[1] == "2" and round[0] == "1":
            win = "yes"
        elif round[1] == "3" and round[0] == "2":
            win = "yes"

    if win=="yes":
        sum+=6
    elif win=="draw":
        sum+=3
    print(sum)
