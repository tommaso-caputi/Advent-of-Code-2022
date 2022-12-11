#  rock  =    A            
#  paper =    B
#  scissors = C
#  1>3, 3>2 2>1
with open("2.txt","r") as f:
    list = f.readlines()
sum = 0
for round in list:
    if round[2] == "X":   #lose
        if round[0]=="A":
            sum+=3
        elif round[0]=="B":
            sum+=1
        else:
            sum+=2
    elif round[2] == "Y": #draw
        sum+=3
        if round[0]=="A":
            sum+=1
        elif round[0]=="B":
            sum+=2
        else:
            sum+=3
    else:                 #win
        if round[0]=="A":
            sum+=6+2
        elif round[0]=="B":
            sum+=6+3
        else:
            sum+=6+1
print(sum)