list = []
a = []
with open('1.txt','r') as f:
    lines = f.readlines()
for line in lines:
    if not line.strip():
        list.append(sum(a))
        a = []
    else:
        a.append(int(line[:-1]))

sum = 0
for i in range(3):
    sum += max(list)
    list.remove(max(list))
print(sum)