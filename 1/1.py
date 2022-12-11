list = []
a = []
with open('1.txt','r') as f:
    lines = f.readlines()
for line in lines:
    if not line.strip():
        print(a, sum(a))
        list.append(sum(a))
        a = []
    else:
        a.append(int(line[:-1]))

print(max(list))