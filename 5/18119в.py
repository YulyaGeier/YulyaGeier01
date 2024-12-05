p=[]
for n in range (1,1000):
    b=
    if (b.count('1')+2*b.count('2'))==0:
        b='1'+b+'2'
    else: b='2'+b+'0'
    r=int(b,3)
    if r>100:
        p.append(r)
print(min(p))