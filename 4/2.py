with open("4.txt","r") as f:
    list = f.readlines()
for i in range(len(list)-1):
    list[i] =list[i][:-1]
sum = 0
for line in list:
    elfs = line.split(",")
    splits = []
    for nums in elfs:
        splits.append(nums.split("-"))
    sections=[]
    sections.append([x for x in range(int(splits[0][0]),int(splits[0][1])+1)])
    sections.append([x for x in range(int(splits[1][0]),int(splits[1][1])+1)])
    check=False
    for num in sections[0]:
        if num in sections[1]:
            check=True
            break
    if check:
        sum+=1
print(sum)  