p=[]
for n in range (1,1000):
    b=bin(n)[2:]
    if n%2 == 0:
        b='10'+str(b)
    else: b = '1'+b+'01'
    r=int(b,2)
    if n<=12:
        p.append(r)
print(max(p))