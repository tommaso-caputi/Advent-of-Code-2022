with open("3.txt","r") as f:
    list = f.readlines()

for i in range(len(list)-1):
    list[i] =list[i][:-1]

common=[]
for i in range(0, len(list)-1, 3):
    a = [set(list[i]),set(list[i+1]),set(list[i+2])]
    s = a[0].intersection(a[1])
    s = s.intersection(a[2])
    common.append(str(s)[2])


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