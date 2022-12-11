with open("5.txt","r") as f:
    list = f.readlines()
for i in range(len(list)-1):
    list[i] =list[i][:-1]
temp_stacks = list[:list.index('')]
moves = list[list.index('')+1:]
stacks = []
for j in range(0,36,4): #0,36,4
    temp=[]
    for i in range(len(temp_stacks)-1):
        if temp_stacks[i][j:j+3]!="   ":
            temp.append(temp_stacks[i][j+1])
    temp = temp[::-1]
    stacks.append(temp)
for move in moves:
    if len(move)>18:
        n = move[5:7]
        fr = move[13]
        to = move[18]
    else:
        to = move[17]
        fr = move[12]
        n = move[5]
    print(n)
    add = stacks[int(fr)-1][-int(n):] # get n to move
    #add = add[::-1]
    stacks[int(fr)-1] = stacks[int(fr)-1][:-int(n)]
    stacks[int(to)-1].append(add) #add move
    stacks[int(to)-1] = [a for b in stacks[int(to)-1] for a in b]
res=""
for stack in stacks:
    res+=str(stack[-1])
print(res)

