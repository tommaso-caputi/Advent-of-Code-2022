with open("6.txt","r") as f:
    signal = f.read()
for i in range(len(signal)-4):
    temp = signal[i:i+4]
    if len(temp)==len(set(temp)):
        res=i+4
        break
print(res)