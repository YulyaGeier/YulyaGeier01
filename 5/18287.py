p=[]
for N in range (1,1000):
    b=bin(N)[2:]
    if (len(str(b))%2)==0:
        b=b+"1"
    else: b="1"+str(b)+"0"
    r=int(b,2)
    if r>666:
        p.append(r)
print(min(p))
