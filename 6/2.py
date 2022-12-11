with open("6.txt","r") as f:
    signal = f.read()
for i in range(len(signal)-14):
    temp = signal[i:i+14]
    if len(temp)==len(set(temp)):
        res=i+14
        break
print(res)