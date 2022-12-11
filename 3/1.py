with open("3.txt","r") as f:
    list = f.readlines()

for i in range(len(list)-1):
    list[i] =list[i][:-1]

common = []
for item in list:
    common.append(str(set(item[:int(len(item)/2)]).intersection(item[int(len(item)/2):]))[2])

sum=0
i=1
values={}
for s in [chr(i) for i in range(ord('a'),ord('z')+1)]:
    values[s]=i
    i+=1
for s in [chr(i) for i in range(ord('a'),ord('z')+1)]:
    values[s.upper()]=i
    i+=1

for el in common:
    sum+=values[el]

print(sum)